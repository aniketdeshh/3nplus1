import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def plot(self):
        plt.xlabel('Steps')
        plt.ylabel('Number')
        plt.title('3N+1')
        plt.plot(self.x, self.y)
        plt.show()

