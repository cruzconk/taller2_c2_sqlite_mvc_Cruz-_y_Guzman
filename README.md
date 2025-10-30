# Gestor de Estudiantes MVC
Proyecto generado automáticamente basado en la Guía 12 (SQLite + MVC).
Estructura:
- modelo/estudiante.py -> funciones de persistencia (SQLite)
- controlador/gestor.py -> lógica de negocio
- vista/main.py -> interfaz por consola (menú)
- main.py -> punto de entrada

Archivos importantes:
- estudiantes.csv -> CSV de ejemplo (si existe)
- estudiantes.db -> base de datos SQLite (se crea al ejecutar la app)

Ejecutar:
1. Asegúrate de tener Python 3.8+.
2. Desde la carpeta del proyecto: `python main.py`
3. Usa el menú por consola para interactuar.

Nota:
- Si quieres importar un CSV existente utiliza la opción 6 del menú.
- El módulo `modelo.estudiante` espera un CSV con columnas: id,nombre,nota,id_curso
