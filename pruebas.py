from red import Red
from agente import Agente
from estrategias.fuerzabruta import FuerzaBruta

class Pruebas:
    def __init__(self):
        pass

    def test_uno(self):
        agentes = [Agente(100, 0.5, 1), Agente(100, 0.1, 1), Agente(-10, 0.1, 1)]
        red = Red(agentes, 55)
        fb = FuerzaBruta(red)
        return fb.solve()

    def test_dos(self):
        agentes = [Agente(-30, 0.9, 1), Agente(20, 0.1, 2), Agente(50, 0.5, 1)]
        red = Red(agentes, 35)
        fb = FuerzaBruta(red)
        return fb.solve()

    def test_tres(self):
        agentes = [Agente(50, 0.5, 1), Agente(-40, 0.2, 2), Agente(10, 0.9, 3)]
        red = Red(agentes, 0)
        fb = FuerzaBruta(red)
        return fb.solve()

    def test_cuatro(self):
        agentes = [Agente(100, 1, 3), Agente(-100, 1, 3)]
        red = Red(agentes, 0)
        fb = FuerzaBruta(red)
        return fb.solve()

    def test_cinco(self):
        agentes = [Agente(40, 0.5, 2), Agente(30, 0.0, 1)]
        red = Red(agentes, 40)
        fb = FuerzaBruta(red)
        return fb.solve()

    def test_seis(self):
        agentes = [Agente(90, 0.0, 1), Agente(-60, 0.5, 3)]
        red = Red(agentes, 90)
        fb = FuerzaBruta(red)
        return fb.solve()

    def test_siete(self):
        agentes = [Agente(7, 0.3, 1.5), Agente(5, 0.8, 1)]
        red = Red(agentes, 8)
        fb = FuerzaBruta(red)
        return fb.solve()

    def test_ocho(self):
        agentes = [Agente(7, 0.3, 1.5), Agente(5, 0.8, 1)]
        red = Red(agentes, 7)
        fb = FuerzaBruta(red)
        return fb.solve()

    def test_nueve(self):
        agentes = [Agente(-100, 0.2, 3), Agente(80, 0.6, 2), Agente(-20, 0.0, 1.2)]
        red = Red(agentes, 500)
        fb = FuerzaBruta(red)
        return fb.solve()