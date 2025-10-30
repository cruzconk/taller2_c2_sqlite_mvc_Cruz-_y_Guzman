from services.gestor_notas import GestorNotas
from csv_utils import exportar_notas_a_csv
from database_utils import crear_base, importar_csv_a_bd, consultar_notas

gestor = GestorNotas()

while True:
    print("\n=== GESTOR DE NOTAS ===")
    print("1. Crear nota")
    print("2. Leer nota")
    print("3. Listar notas")
    print("4. Eliminar nota")
    print("5. Editar nota")
    print("6. Exportar a JSON")
    print("7. Guardar notas en binario (Pickle)")
    print("8. Cargar notas desde binario (Pickle)")
    print("9. Exportar notas a CSV (Guía 11)")
    print("10. Importar CSV a SQLite (Guía 11)")
    print("11. Consultar notas en SQLite (Guía 11)")
    print("0. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la nota: ")
        contenido = input("Contenido: ")
        from models.nota import Nota
        nota = Nota(nombre, contenido)
        gestor.guardar(nota)
        print("✅ Nota creada.")
    elif opcion == "2":
        nombre = input("Nombre de la nota a leer: ")
        print(gestor.leer(nombre))
    elif opcion == "3":
        print("📋 Notas disponibles:", gestor.listar())
    elif opcion == "4":
        nombre = input("Nombre de la nota a eliminar: ")
        if gestor.eliminar(nombre):
            print("🗑️ Nota eliminada correctamente.")
    elif opcion == "5":
        nombre = input("Nombre de la nota a editar: ")
        nuevo = input("Nuevo contenido: ")
        if gestor.editar(nombre, nuevo):
            print("✏️ Nota actualizada.")
    elif opcion == "6":
        gestor.exportar_json()
    elif opcion == "7":
        from repositories.pickle_repository import PickleRepository
        repo = PickleRepository()
        notas = {n: gestor.leer(n) for n in gestor.listar()}
        repo.guardar(notas)
        print("💾 Notas guardadas en binario (Pickle).")
    elif opcion == "8":
        from repositories.pickle_repository import PickleRepository
        repo = PickleRepository()
        datos = repo.cargar()
        for nombre, contenido in datos.items():
            from models.nota import Nota
            nota = Nota(nombre, contenido)
            gestor.guardar(nota)
        print("📂 Notas cargadas desde archivo binario.")
    elif opcion == "9":
        exportar_notas_a_csv()
    elif opcion == "10":
        crear_base()
        importar_csv_a_bd()
    elif opcion == "11":
        consultar_notas(longitud_minima=15)
    elif opcion == "0":
        print("👋 Saliendo del programa...")
        break
    else:
        print("❌ Opción no válida.")
