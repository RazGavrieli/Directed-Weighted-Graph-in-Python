from random import randint

from src.GraphAlgo import GraphAlgo
from time import time


def loadPerformance():
    g = GraphAlgo()

    s = time()
    b = g.load_from_json("testData/1m.json")
    f = time()

    overall = f-s
    print("finished in ", overall, " and it ", b)

def centerPerformance():
    g = GraphAlgo()
    g.load_from_json("testData/10k.json")
    s = time()
    x = g.centerPoint()
    f = time()

    overall = f-s
    print("finished in ", overall, "\n center is ", x)

def createK(k: int):
    nodesize = 1000*k
    g = GraphAlgo()
    for i in range(nodesize):
        g.get_graph().add_node(i)

    for i in range(nodesize):
        for j in range(10):
            dest = randint(0,nodesize)
            w = randint(1, 5)
            g.get_graph().add_edge(i, dest, w)
    g.save_to_json("testData/-INSERT NEW NAME HERE-.json")


if __name__ == '__main__':
   loadPerformance()