import pickle
import datetime

#resultados = []
class Resultado:

    def __init__(self, jugador, puntos):
        self.fecha = datetime.datetime.now()
        self.jugador = jugador
        self.puntos = puntos

    def imprimir(self):
        print(str(self.fecha) + " " + self.jugador + " " + str(self.puntos))




def guardar_resultados(resultados):
    with open("resultados.pickle", "wb") as archivo_resultados:
        pickle.dump(resultados, archivo_resultados)

def cargar_resultados():
    try:
        with open("resultados.pickle", "rb") as archivo_resultados:
            return pickle.load(archivo_resultados)
    except:
        return []