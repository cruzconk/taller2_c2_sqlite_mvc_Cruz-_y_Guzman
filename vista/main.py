"""vista/main.py
Interfaz por consola para interactuar con el Gestor de Estudiantes.
"""
from controlador import gestor

def mostrar_menu():
    menu = [
        "1. Agregar estudiante",
        "2. Listar estudiantes",
        "3. Actualizar nota",
        "4. Eliminar registros por nota (umbral)",
        "5. Buscar por nombre",
        "6. Importar desde CSV",
        "7. Salir"
    ]
    print("\nGestor de Estudiantes - MVC\n")
    for opcion in menu:
        print(opcion)

def leer_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Por favor ingrese un número válido.")

def main():
    gestor.inicializar()
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()
        if opcion == '1':
            nombre = input("Nombre: ").strip()
            nota = leer_float("Nota: ")
            gestor.agregar_estudiante(nombre, nota)
            print("Estudiante agregado correctamente.")
        elif opcion == '2':
            orden = input("Ordenar por nota descendente? (s/n): ").lower().startswith('s')
            rows = gestor.listar_estudiantes(order_desc=orden)
            if not rows:
                print("No hay estudiantes registrados.")
            else:
                for r in rows:
                    print(f"{r['id']}: {r['nombre']} - {r['nota']}")
        elif opcion == '3':
            nombre = input("Nombre del estudiante a actualizar: ").strip()
            nueva = leer_float("Nueva nota: ")
            afect = gestor.actualizar_nota(nombre, nueva)
            if afect:
                print("Nota actualizada.")
            else:
                print("No se encontró un estudiante con ese nombre.")
        elif opcion == '4':
            umbral = leer_float("Eliminar estudiantes con nota menor a: ")
            afect = gestor.eliminar_por_nota(umbral)
            print(f"Registros eliminados: {afect}")
        elif opcion == '5':
            sub = input("Buscar nombre (subcadena): ").strip()
            rows = gestor.buscar_por_nombre(sub)
            if not rows:
                print("No se encontraron coincidencias.")
            else:
                for r in rows:
                    print(f"{r['id']}: {r['nombre']} - {r['nota']}")
        elif opcion == '6':
            path = input("Ruta al archivo CSV: ").strip()
            try:
                gestor.inicializar(csv_path=path)
                print("Importación completada (si el CSV era válido).")
            except Exception as e:
                print("Error al importar CSV:", e)
        elif opcion == '7':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == '__main__':
    main()
