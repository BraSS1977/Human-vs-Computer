import random

class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.first_attack = True  # Флаг для отслеживания первого удара

    def attack(self, other):
        if self.first_attack:
            # Первый удар фиксированной силой 20
            damage = 20
            self.first_attack = False  # Устанавливаем флаг на False после первого удара
        else:
            # Последующие удары составляют 25% от оставшегося здоровья
            damage = self.health * 0.25

        # Наносим урон другому герою
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит урон в {damage:.2f} единиц.")

        # Обеспечиваем, чтобы здоровье не уходило ниже нуля
        if other.health < 0:
            other.health = 0

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name="Игрок", computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Игра начинается!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} побежден!")
                print(f"Победитель: {self.player.name}")
                break
            print(f"{self.computer.name} имеет {self.computer.health:.2f} здоровья.\n")

            # Ход компьютера, наносящий 25% урона от оставшегося здоровья игрока
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} побежден!")
                print(f"Победитель: {self.computer.name}")
                break
            print(f"{self.player.name} имеет {self.player.health:.2f} здоровья.\n")

# Запуск игры
game = Game(player_name="Воин", computer_name="Компьютер")
game.start()