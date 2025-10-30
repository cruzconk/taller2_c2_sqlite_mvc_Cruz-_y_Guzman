import os
import json
from models.nota import Nota

class GestorNotas:
    def __init__(self, carpeta="notas"):
        self.carpeta = carpeta
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

    def guardar(self, nota):
        try:
            ruta = os.path.join(self.carpeta, f"{nota.nombre}.txt")
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(nota.contenido)
            return True
        except Exception as e:
            print("Error al guardar la nota:", e)
            return False

    def leer(self, nombre):
        try:
            ruta = os.path.join(self.carpeta, f"{nombre}.txt")
            with open(ruta, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "Nota no encontrada."

    def listar(self):
        try:
            archivos = [f[:-4] for f in os.listdir(self.carpeta) if f.endswith(".txt")]
            return archivos
        except Exception as e:
            print("Error al listar notas:", e)
            return []

    def eliminar(self, nombre):
        try:
            ruta = os.path.join(self.carpeta, f"{nombre}.txt")
            if os.path.exists(ruta):
                os.remove(ruta)
                return True
            return False
        except Exception as e:
            print("Error al eliminar nota:", e)
            return False

    def editar(self, nombre, nuevo_contenido):
        try:
            ruta = os.path.join(self.carpeta, f"{nombre}.txt")
            if os.path.exists(ruta):
                with open(ruta, "w", encoding="utf-8") as f:
                    f.write(nuevo_contenido)
                return True
            return False
        except Exception as e:
            print("Error al editar nota:", e)
            return False

    def exportar_json(self, archivo_json="notas.json"):
        try:
            notas_data = []
            for nombre in self.listar():
                ruta = os.path.join(self.carpeta, f"{nombre}.txt")
                with open(ruta, "r", encoding="utf-8") as f:
                    contenido = f.read()
                    notas_data.append({
                        "nombre": nombre,
                        "contenido": contenido
                    })
            with open(archivo_json, "w", encoding="utf-8") as fjson:
                json.dump(notas_data, fjson, ensure_ascii=False, indent=4)
            print(f"Notas exportadas a {archivo_json} correctamente.")
        except Exception as e:
            print("Error al exportar a JSON:", e)
