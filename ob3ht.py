class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        return "Chirp chirp"

    def eat(self):
        return "Seeds and insects"


class Mammal(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return "Roar"

    def eat(self):
        return "Plants and meat"


class Reptile(Animal):
    def __init__(self, name, age, length):
        super().__init__(name, age)
        self.length = length

    def make_sound(self):
        return "Hiss"

    def eat(self):
        return "Insects"

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

# Пример использования
bird = Bird("Parrot", 5, 20)
mammal = Mammal("Lion", 7, "Yellow")
reptile = Reptile("Snake", 3, 100)

animals = [bird, mammal, reptile]
animal_sound(animals)