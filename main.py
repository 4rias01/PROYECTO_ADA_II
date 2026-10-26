from agente import Agente
from red import Red
from estrategias.fuerzabruta import FuerzaBruta
from pruebas import Pruebas

def generar_agentes(num_agentes):
    agentes = []
    for i in range(num_agentes):
        agentes.append(Agente())

    return agentes

if __name__ == '__main__':
    p = Pruebas()
    print(p.test_uno())
    