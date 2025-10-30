import sqlite3
import csv
import os

def crear_base(nombre_bd="notas.db"):
    conn = sqlite3.connect(nombre_bd)
    cur = conn.cursor()
    cur.execute("""        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            contenido TEXT NOT NULL,
            longitud INTEGER
        )
    """)
    conn.commit()
    conn.close()
    print(f"✅ Base de datos {nombre_bd} lista.")

def importar_csv_a_bd(nombre_csv="notas.csv", nombre_bd="notas.db"):
    if not os.path.exists(nombre_csv):
        print("⚠️ No existe el archivo CSV para importar.")
        return

    conn = sqlite3.connect(nombre_bd)
    cur = conn.cursor()
    with open(nombre_csv, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            cur.execute(
                "INSERT INTO notas (nombre, contenido, longitud) VALUES (?, ?, ?)",
                (fila["nombre"], fila["contenido"], int(fila["longitud"]))
            )
    conn.commit()
    conn.close()
    print(f"✅ Datos importados correctamente desde {nombre_csv}.")

def consultar_notas(longitud_minima=20, nombre_bd="notas.db"):
    conn = sqlite3.connect(nombre_bd)
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, longitud FROM notas WHERE longitud >= ?", (longitud_minima,))
    resultados = cur.fetchall()
    conn.close()

    print(f"\n📘 Notas con longitud >= {longitud_minima} caracteres:")
    print("--------------------------------------------")
    for id_nota, nombre, longitud in resultados:
        print(f"[{id_nota}] {nombre} ({longitud} caracteres)")

# Ventajas y limitaciones según guía:
# Ventajas:
# - Consultas SQL estructuradas.
# - Persistencia y consistencia de datos.
# - No requiere servidor externo.
# Limitaciones:
# - No es multiusuario concurrente.
# - Tamaño del archivo crece con los datos.
