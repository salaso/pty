import time as t
import mazo.cartas as cs
import mazo.resultados as rs
import random
import sys
#import datetime as dt

puntuaciones = rs.cargar_resultados()
palo_debil = random.choice(["Diamantes", "Corazones", "Treboles", "Rombos"])
palo_fuerte = random.choice(["Corazones", "Diamantes", "Treboles", "Rombos"])


def jugar(nombre):
    global palo_debil
    global palo_fuerte

    while True:
        print("Generando Mazo...")
        t.sleep(2)
        nuevo_mazo = cs.crear_mazo()
        print("Revolviendo Mazo...")
        t.sleep(2)
        cs.revolver_mazo()
        print("Obteniendo 10 cartas para... " + nombre)
        primer_grupo = cs.sacar_cartas(10, cs.revolver_mazo())
        cartas_usuario = primer_grupo[0]
        t.sleep(2)
        print("obteniendo 10 ocultas... ")
        segundo_grupo = cs.sacar_cartas(10, cs.revolver_mazo())
        grupo_oculto = segundo_grupo[1]
        print("Las 10 cartas ocultas estan listas!")
        t.sleep(1)
        print("\nDeterminando palo fuerte y palo debil...")
        t.sleep(2)
        print("El Palo debil es: " + palo_debil)
        print("El Palo fuerte es: " + palo_fuerte)
        t.sleep(2)
        print("\nSus cartas son: ")
        n = 0
        for c in primer_grupo[0]:
            print(primer_grupo[0][n])
            n = n + 1
        t.sleep(2)

        encuentros = 0
        while True:
            try:
                encuentros = int(input("Indique el numero de encuentros que cree que va a ganar de entre 0 y 10: "))
                if(encuentros >= 0 and encuentros <= 10):
                    break
                else:
                    print("Valor invalido, debe ser un valor entre  y 10")

            except:
                print("Valor incorrecto!")

        print("Realizando encuentros! ")
        t.sleep(3)

        print("\n***Resultados***")
        victorias = 0

        for encuentro in range(10):
            t.sleep(2)
            carta_usuario = cartas_usuario[encuentro]
            carta_oculta = grupo_oculto[encuentro]


            imprimir = str(carta_usuario) + " vs " + str(carta_oculta)
            if(resolver_encuentro(carta_usuario, carta_oculta)):
                imprimir = imprimir+": Has Ganado!"
                victorias = victorias +1
                print(imprimir)
            else:
                imprimir = imprimir + ": perdiste!"
                print(imprimir)
        print("Total de victorias: "+str(victorias))
        print("Apuesta: "+str(encuentros))
        final = 10-abs(encuentros-victorias)
        print("Puntuacion final: " + str(final))

        puntuaciones.append(rs.Resultado(nombre, final))
        rs.guardar_resultados(puntuaciones)
        break

def resolver_encuentro(carta_j, carta_o):
    if(carta_j.Palo == carta_o.Palo):
        return carta_j.Valor >= carta_o.Valor
    elif(carta_j.Palo == palo_fuerte):
        return carta_o.Palo != palo_debil
    elif (carta_j.Palo == palo_debil):
        return carta_o.Palo == palo_fuerte
    else:
        if(carta_o.Palo == palo_debil):
            return True
        elif(carta_o.Palo == palo_fuerte):
            return False
        else:
            return carta_j.Valor >= carta_o.Valor



def menu(nombre):
    while True:
        try:
            print("=== Menu ===")
            print("Ingrese la opción deseada:")
            print("1. Iniciar Juego")
            print("2. Ver Puntuaciones")
            print("3. Salir")
            opcion = input("Opcion: ")

            if(opcion == "1"):
                jugar(nombre)
                break
            elif(opcion == "2"):
                for n in puntuaciones:
                    n.imprimir()
                break

            elif(opcion == "3"):
                exit()
                
            else:
                print("Opción no válida!")
        except:
            print("Except - Opcion invalida!")


if(__name__ == "__main__"):
    try:

        nombre = sys.argv[1]
        menu(nombre)

    except Exception as e:
        print(e)
        print("Debe ingresar su nombre")
        print("Ejemplo:")
        print("    python juego.py Oscar")
