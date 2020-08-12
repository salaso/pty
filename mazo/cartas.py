import random
class Cartas:

    def __init__(self, Valor = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13]), Palo = random.choice(["Diamantes", "Corazones", "Treboles", "Rombos"])):
        self.Valor = Valor
        self.Palo = Palo

    def imprimir(self):
        if self.Valor == 11:
            print("Jota de " + self.Palo)
        elif self.Valor == 12:
            print("Reina de " + self.Palo)
        elif self.Valor == 13:
            print("Rey de " + self.Palo)
        else:
            print(str(self.Valor) + " de " + self.Palo)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.Valor} de {self.Palo}"

#carta = Cartas()
#carta.imprimir()

def crear_mazo():
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    lista_tipos = ["Rombos", "Corazones", "Treboles", "Diamantes"]
    lista_mazo = []
    for numero in lista_numeros:
        for tipo in lista_tipos:
            lista_mazo.append(Cartas(numero, tipo))
    return lista_mazo

#print(crear_mazo())


def revolver_mazo():
    lista_revuelta = random.sample(crear_mazo(), 52)
    return lista_revuelta
#print(revolver_mazo())


def sacar_cartas(N, lista_cartas):
    lista_N = []
    lista2_N = []
    for i in range(N):
        lista_N.append(lista_cartas.pop(0))
        lista2_N.append(lista_cartas.pop(0))
    #tupla = tuple([lista_N, lista2_N])
    return (lista_N, lista2_N)

#print(sacar_cartas(10, revolver_mazo()))









