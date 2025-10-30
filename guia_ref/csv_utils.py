import csv
import os

def exportar_notas_a_csv(carpeta_notas="notas", nombre_csv="notas.csv"):
    if not os.path.exists(carpeta_notas):
        print("⚠️ No existe la carpeta de notas.")
        return

    archivos = [f for f in os.listdir(carpeta_notas) if f.endswith(".txt")]
    if not archivos:
        print("⚠️ No hay notas para exportar.")
        return

    with open(nombre_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nombre", "contenido", "longitud"])
        for archivo in archivos:
            ruta = os.path.join(carpeta_notas, archivo)
            with open(ruta, "r", encoding="utf-8") as nota:
                contenido = nota.read()
                writer.writerow([archivo[:-4], contenido, len(contenido)])

    print(f"✅ Notas exportadas correctamente a {nombre_csv}.")
