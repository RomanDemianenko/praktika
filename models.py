from random import randint
from exceptions import EnemyDown, GameOver
import settings


class Enemy:
    '''Прописуем атрибуты и методы врага'''

    def __init__(self, enemy_level):
        self.enemy_level = enemy_level
        self.enemy_lives = enemy_level

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decrease_lives(self):
        self.enemy_lives -= 1
        if self.enemy_lives == 0:
            raise EnemyDown


class Player:
    '''Прописуем атрибуты и методы игрока'''

    def __init__(self, player_name):
        self.player_name = player_name
        self.player_lives = settings.PLAYER_LIVES
        self.player_score = 0
        self.allowed_attacks = [1, 2, 3]

    @staticmethod
    def fight(attack, defence):
        if attack == defence:
            return 0
        elif attack == 1 and defence == 2:
            return 1
        elif attack == 2 and defence == 3:
            return 1
        elif attack == 3 and defence == 1:
            return 1
        else:
            return -1

    def decrease_lives(self):
        self.player_lives -= 1
        if self.player_lives == 0:
            raise GameOver(self)

    def attack(self, enemy):
        attack = None
        while attack not in self.allowed_attacks:
            try:
                attack = int(input("Select Attack to Use: 1 - WIZARD, 2 - WARRIOR, 3 - ROGUE: "))
                if attack not in self.allowed_attacks:
                    raise ValueError
            except ValueError:
                print("Incorrect input!")
        self.fight(attack, enemy.select_attack())
        if self.fight(attack, enemy.select_attack()) == 0:
            print('It`s a draw!')
        elif self.fight(attack, enemy.select_attack()) == 1:
            print('Your attacked successfully')
            enemy.decrease_lives()
        else:
            print('You missed')

    def defence(self, enemy):
        defence = None
        while defence not in self.allowed_attacks:
            try:
                defence = int(input("Select Defence to Use: 1 - WIZARD, 2 - WARRIOR, 3 - ROGUE: "))
                if defence not in self.allowed_attacks:
                    raise ValueError
            except ValueError:
                print("Incorrect input!")
        self.fight(enemy.select_attack(), defence)
        if self.fight(enemy.select_attack(), defence) == 0:
            print('It`s a draw!')
        elif self.fight(enemy.select_attack(), defence) == 1:
            print('You lost')
            self.decrease_lives()
        else:
            print('You defended successfull')
