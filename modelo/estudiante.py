"""modelo/estudiante.py
Módulo responsable de la persistencia (SQLite) para el Gestor de Estudiantes.
Contiene funciones para crear la base, insertar, listar, actualizar y eliminar registros.
"""
import sqlite3
from pathlib import Path
import csv

DB_PATH = Path(__file__).resolve().parents[1] / "estudiantes.db"

def conectar():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con

def crear_base():
    con = conectar()
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nota REAL,
        id_curso INTEGER
    )""")
    con.commit()
    con.close()

def insertar_estudiante(nombre, nota, id_curso=None):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO estudiantes (nombre, nota, id_curso) VALUES (?, ?, ?)", (nombre, nota, id_curso))
    con.commit()
    con.close()

def listar_estudiantes(order_desc=False):
    con = conectar()
    cur = con.cursor()
    if order_desc:
        cur.execute("SELECT id, nombre, nota, id_curso FROM estudiantes ORDER BY nota DESC")
    else:
        cur.execute("SELECT id, nombre, nota, id_curso FROM estudiantes")
    rows = cur.fetchall()
    con.close()
    return [dict(r) for r in rows]

def actualizar_nota(nombre, nueva_nota):
    con = conectar()
    cur = con.cursor()
    cur.execute("UPDATE estudiantes SET nota = ? WHERE nombre = ?", (nueva_nota, nombre))
    con.commit()
    affected = cur.rowcount
    con.close()
    return affected

def eliminar_por_nota(umbral):
    con = conectar()
    cur = con.cursor()
    cur.execute("DELETE FROM estudiantes WHERE nota < ?", (umbral,))
    con.commit()
    affected = cur.rowcount
    con.close()
    return affected

def buscar_por_nombre(subcadena):
    con = conectar()
    cur = con.cursor()
    pattern = f"%{subcadena}%"
    cur.execute("SELECT id, nombre, nota, id_curso FROM estudiantes WHERE nombre LIKE ?", (pattern,))
    rows = cur.fetchall()
    con.close()
    return [dict(r) for r in rows]

def importar_csv(csv_path):
    # Espera un CSV con columnas: id,nombre,nota,id_curso
    crear_base()
    con = conectar()
    cur = con.cursor()
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("INSERT INTO estudiantes (id, nombre, nota, id_curso) VALUES (?, ?, ?, ?)",
                        (row.get('id'), row.get('nombre'), row.get('nota'), row.get('id_curso')))
    con.commit()
    con.close()
