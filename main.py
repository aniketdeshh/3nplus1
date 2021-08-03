from algorithm import Algorithm
from plot import Plotter

current = int(input('Enter a positive integer >> '))

algo = Algorithm(current)
algo.loop()

x = [i for i in range(1, len(algo.nums)+1)]
y = algo.nums

graph = Plotter(x, y)
graph.plot()