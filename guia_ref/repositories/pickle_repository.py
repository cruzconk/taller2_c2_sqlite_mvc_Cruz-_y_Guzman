import pickle
from pathlib import Path

class PickleRepository:
    def __init__(self, archivo="notas.pkl"):
        self.archivo = Path(archivo)

    def guardar(self, notas):
        with self.archivo.open("wb") as f:
            pickle.dump(notas, f, protocol=pickle.HIGHEST_PROTOCOL)

    def cargar(self):
        if not self.archivo.exists():
            return {}
        with self.archivo.open("rb") as f:
            return pickle.load(f)
