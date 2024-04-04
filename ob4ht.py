from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "удар мечом"


class Bow(Weapon):
    def attack(self):
        return "удар из лука"


class Fighter:
    def __init__(self, weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        return f"Боец наносит {self.weapon.attack()}"


class Monster:
    def __init__(self):
        pass


def battle(fighter, monster):
    print("Боец выбирает", fighter.weapon.__class__.__name__.lower())
    print(fighter.attack())
    print("Монстр побежден!")


sword = Sword()
bow = Bow()

fighter = Fighter(sword)
monster = Monster()

battle(fighter, monster)

fighter.changeWeapon(bow)
battle(fighter, monster)