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

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)


class Employee:
    def __init__(self, name):
        self.name = name


class ZooKeeper(Employee):
    def feed_animal(self, animal):
        return f"{self.name} is feeding {animal.name}"


class Veterinarian(Employee):
    def heal_animal(self, animal):
        return f"{self.name} is healing {animal.name}"


# Пример использования
zoo = Zoo()

bird = Bird("Parrot", 5, 20)
mammal = Mammal("Lion", 7, "Yellow")
reptile = Reptile("Snake", 3, 100)

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zookeeper = ZooKeeper("John")
veterinarian = Veterinarian("Alice")

zoo.add_employee(zookeeper)
zoo.add_employee(veterinarian)

for animal in zoo.animals:
    print(animal.make_sound())

for employee in zoo.employees:
    if isinstance(employee, ZooKeeper):
        print(employee.feed_animal(zoo.animals[0]))
    elif isinstance(employee, Veterinarian):
        print(employee.heal_animal(zoo.animals[1]))


#Этот код создает классы Zoo, Employee, ZooKeeper и Veterinarian с методами
# для добавления животных и сотрудников в зоопарк, а также для кормления и
# лечения животных. В конце программа демонстрирует работу методов на примере
# создания зоопарка с животными и сотрудниками.