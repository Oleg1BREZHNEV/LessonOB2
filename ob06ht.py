#Вот пример программы, реализующей текстовую боевую игру "Битва героев"
# на Python с использованием классов:

import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Computer")

    def start(self):
        current_turn = self.player
        next_turn = self.computer

        while self.player.is_alive() and self.computer.is_alive():
            print(f"{current_turn.name} attacks {next_turn.name}")
            current_turn.attack(next_turn)
            print(f"{next_turn.name} health: {next_turn.health}\n")

            current_turn, next_turn = next_turn, current_turn

        if self.player.is_alive():
            print(f"{self.player.name} wins!")
        else:
            print("Computer wins!")

# Игра
player_name = input("Введите имя игрока: ")
game = Game(player_name)
game.start()


#Просто скопируйте этот код в среду разработки Python (например, PyCharm)
# и запустите его. После запуска программы, следуйте инструкциям на экране,
# чтобы выбрать имя игрока и начать игру. После каждого хода будет отображаться
# информация о текущем здоровье каждого героя и победитель будет
# объявлен в конце игры.
#Удачи в игре "Битва героев"!