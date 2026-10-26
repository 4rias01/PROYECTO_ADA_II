from agente import Agente
from math import sqrt

class Red:
    def __init__(self, num_agentes, r_max):
        self.agentes = []
        self.num_agentes = num_agentes
        for i in range(num_agentes):
            self.agentes.append(Agente())
        self.rmax = r_max

    def get_extremismo(self, estrategia=None):
        sumatoria = 0
        if estrategia == None:
            for agente in self.agentes:
                op = agente.get_opinion()
                inf = agente.get_influencia()

                sumatoria += op**2 * inf
        else:
            for i in range(self.num_agentes):
                agente = self.agentes[i]
                e_i = estrategia[i]
                op = agente.get_opinion() - (1 * e_i)
                inf = agente.get_influencia()
                
                sumatoria += op**2 * inf
                

        resultado = sqrt(sumatoria) / self.num_agentes
        return resultado

    def get_agentes(self):
        return self.agentes

    def get_num_agentes(self):
        return self.num_agentes

    def get_rmax(self):
        return self.rmax
