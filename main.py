from agente import Agente
from red import Red
from estrategias.fuerzabruta import FuerzaBruta

if __name__ == '__main__':
    agen = Agente()
    red = Red(3, 100)
    fb = FuerzaBruta(red)
    print(fb.solve())

    #op = agen.get_opinion()
    #re = agen.get_receptividad()
    #inf = agen.get_influencia()

    #print(f"Opinion: {op}\nReceptividad: {re}\nInfluencia: {inf}")

    #print(red.get_extremismo())