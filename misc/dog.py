from animal import Animal

class Dog(Animal):

    def make_noise(self):
        print("woof")

    def eat(self, food):
        print(f"{self.name} is eating {food} appetitly.")

dog = Dog("Fido")
dog.make_noise()
dog.walk(1, 2)
dog.eat("meat")