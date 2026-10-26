import random

class Agente:

    def __init__(self, opinion=None, receptividad=None, influencia=None):
        if opinion == None or receptividad == None or influencia == None:
            self.opinion = random.randint(-100, 100)
            self.receptividad = random.uniform(0, 1)
            self.influencia = random.uniform(1,3)
        else:
            self.opinion = opinion
            self.receptividad = receptividad
            self.influencia = influencia

    def get_opinion(self):
        return self.opinion

    def get_receptividad(self):
        return self.receptividad

    def get_influencia(self):
        return self.influencia

    def set_opinion(self, op):
        self.opinion = op

    def set_receptividad(self, re):
        self.receptividad = re

    def set_influencia(self, inf):
        self.influencia = inf

