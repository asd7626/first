import random
import math

#name = input("Имя персонажа: ")
#power = int(input("Сила: "))
#agility = int(input("Ловкость: "))
#luck = int(input("Удача: "))


class Character:

    def __init__(self, power, agility, luck):
        self.power = power
        self.agility = agility
        self.luck = luck
        self.health = self.power * 10
        self.defence = self.agility * 5
        self.attack_speed = 60 / self.agility # перерыв между атаками
        self.level = 0
        self.punch = 0

    def hit(self, other):
        self.punch = random.randrange(math.ceil((self.power + self.agility) / 2),
                                  int(self.power * 2) + 1, 1)
        other.lose_hp(self.punch)

    def lose_hp(self, x):
        self.health = self.health - x


class Monster:

    def __init__(self):
        self.power = random.randrange(3, 10, 1)
        self.agility = random.randrange(3, 10, 1)
        self.luck = random.randrange(3, 10, 1)
        self.health = self.power * 10
        self.defence = self.agility * 5
        self.attack_speed = 60 / self.agility  # перерыв между атаками
        self.punch = 0

    def hit(self, other):
        self.punch = random.randrange(math.ceil((self.power + self.agility) / 2),
                                      int(self.power * 2) + 1, 1)
        other.lose_hp(self.punch)

    def lose_hp(self, x):
        self.health = self.health - x


class Fight:

    @staticmethod
    def start_the_fight(character, monster):
        character_punch_count = 0
        monster_punch_count = 0
        print('Бой начался. У Игрока {} хп, у Монстра {} хп'.format(character.health, monster.health))
        while character.health > 0 or monster.health > 0:

            if monster.health > 0:
                character_punch_count += 1
            character.hit(monster)

            if character.health > 0:
                monster_punch_count += 1
            monster.hit(character)

        print('Кол-во ударов Персонажа: ', character_punch_count)
        print('Кол-во ударов Монстра: ', monster_punch_count)

        total_time_character = character_punch_count * character.attack_speed
        total_time_monster = monster_punch_count * monster.attack_speed
        print('Общее время Персонажа:' , total_time_character, 'секунд')
        print('Общее время Монстра:', total_time_monster, 'секунд')

        if total_time_character < total_time_monster:
            winner = character
            print('Персонаж победил')
        else:
            winner = monster
            print('Монстр победил')


c = Character(10, 10, 7)
m = Monster()
f = Fight()
f.start_the_fight(c, m)