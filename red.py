from agente import Agente
from math import sqrt

class Red:
    def __init__(self, num_agentes, r_max):
        self.agentes = []
        self.num_agentes = num_agentes
        for i in range(num_agentes):
            self.agentes.append(Agente())
        self.r_max = r_max

    def get_extremismo(self):
        sumatoria = 0
        for agente in self.agentes:
            op = agente.get_opinion()
            inf = agente.get_influencia()

            sumatoria += op**2 * inf

        resultado = sqrt(sumatoria) / self.num_agentes

    def get_agentes(self):
        return self.agentes

    def get_num_agentes(self):
        return self.num_agentes
