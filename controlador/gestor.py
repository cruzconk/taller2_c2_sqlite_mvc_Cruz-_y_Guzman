"""controlador/gestor.py
Lógica de negocio que coordina las operaciones entre la vista y el modelo.
"""
from modelo import estudiante

def inicializar(csv_path=None):
    # Crear la base si no existe y opcionalmente importar CSV
    estudiante.crear_base()
    if csv_path:
        try:
            estudiante.importar_csv(csv_path)
        except Exception:
            # si la importación falla, se ignora para permitir inicialización
            pass

def agregar_estudiante(nombre, nota, id_curso=None):
    estudiante.insertar_estudiante(nombre, nota, id_curso)
    return True

def listar_estudiantes(order_desc=False):
    return estudiante.listar_estudiantes(order_desc=order_desc)

def actualizar_nota(nombre, nueva_nota):
    return estudiante.actualizar_nota(nombre, nueva_nota)

def eliminar_por_nota(umbral):
    return estudiante.eliminar_por_nota(umbral)

def buscar_por_nombre(subcadena):
    return estudiante.buscar_por_nombre(subcadena)
