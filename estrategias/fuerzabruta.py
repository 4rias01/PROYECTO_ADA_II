from red import Red

def techo(x):
    
    if x == int(x):
        return int(x)
    elif x > 0:
        return int(x) + 1
    else:
        return int(x)

def esfuerzo(red: Red, estrategia: list[int]):
    agentes = red.get_agentes()
    sumatoria = 0

    for i, agente in enumerate(agentes):
        e_i = estrategia[i]
        op = agente.get_opinion()
        op_prima = op * (1 - e_i)
        rc = agente.get_receptividad()
        inf = agente.get_influencia()

        sumatoria += techo(abs(op - op_prima) * (1 - rc) * inf)

    return sumatoria

def generar_estrategias(num_agentes):
    if num_agentes <= 0:
        return [[]]
    else:
        estrategias = generar_estrategias(num_agentes-1)
        parte1 = [[1] + estrategia for estrategia in estrategias]
        parte2 = [[0] + estrategia for estrategia in estrategias] 
        return list(parte1 + parte2)



class FuerzaBruta:
    def __init__(self, red: Red):
        self.red = red

    def solve(self):
        esfuerzo_max = self.red.get_rmax()
        estrategias = generar_estrategias(self.red.get_num_agentes())
        esfuerzo_final = 0
        extremismo_final = float("inf")
        estrategia_final = None

        for estrategia in estrategias:
            esf = esfuerzo(self.red, estrategia)
            extremismo = self.red.get_extremismo(estrategia)

            if esf <= esfuerzo_max and extremismo < extremismo_final:
                esfuerzo_final = esf
                extremismo_final = extremismo
                estrategia_final = estrategia

        return [esfuerzo_final, extremismo_final, estrategia_final]



