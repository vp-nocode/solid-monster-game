from abc import ABC, abstractmethod
import random


class Weapon(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):

    def attack(self):
        impact_force = random.randint(10, 20)
        return ["strikes with a sword", impact_force]


class Bow(Weapon):

    def attack(self):
        impact_force = random.randint(3, 12)
        return ["shoots from a bow", impact_force]


class Fighter:

    def __init__(self, name: str):
        self.__name = name
        self.__weapon = None

    def type_of_weapon(self):
        return self.__weapon.__class__.__name__

    def fight(self):
        attack = self.__weapon.attack()
        print(f"The fighter {self.__name} {attack[0]} with an impact force of {attack[1]}")
        return attack[1]

    def change_weapon(self, weapon: Weapon):
        self.__weapon = weapon
        print(f"The fighter {self.__name} chooses a {self.__weapon.__class__.__name__}")


class Monster:

    def __init__(self):
        self.__health = 100

    def status(self):
        if self.__health <= 0:
            print("The monster is defeated (0 ball)")
        elif self.__health < 50:
            print(f"The monster is weak ({self.__health} ball)")
        else:
            print(f"The monster is strong ({self.__health} ball)")
        return self.__health

    def change_health(self, value: int):
        self.__health += value

# game
fighter = Fighter("Lancelot")
monster = Monster()
distance = random.randint(50, 100)
print(f"The distance is {distance} meters")
print("The fighter begin to fight")

while True:

    if distance <= 3:
        if fighter.type_of_weapon() != "Sword":
            fighter.change_weapon(Sword())
    else:
        if fighter.type_of_weapon() != "Bow":
            fighter.change_weapon(Bow())

    impact_force = fighter.fight()
    monster.change_health(-impact_force)

    if monster.status() <= 0:
        break

    distance = distance -random.randint(5, 10)
    if distance <= 0:
        distance = 0
    print(f"The monster's distance is {distance} meters")
