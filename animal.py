class Animal:
    def __init__(self, name):
        self.name = name
        self.position = [0, 0]

    def walk(self, x, y):
        self.position[0] += x
        self.position[1] += y
        print(f"{self.name} is walking to ({self.position[0]}, {self.position[1]})")

    def eat(self, food):
        print(f"{self.name} is eating {food}")