from agente import Agente

if __name__ == '__main__':
    agen = Agente()
    op = agen.get_opinion()
    re = agen.get_receptividad()
    inf = agen.get_influencia()

    print(f"Opinion: {op}\nReceptividad: {re}\nInfluencia: {inf}")