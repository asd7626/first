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
        self.attack_speed = 60 / self.agility  # перерыв между атаками
        self.level = 0
        self.punch = 0

    def hit(self, other):
        self.punch = random.randrange(math.ceil((self.power + self.agility) / 2),
                                  int(self.power * 2) + 1, 1)
        other.lose_hp(self.punch)

    def lose_hp(self, x):
        self.health = self.health - x

    def recover(self):
        self.health = self.power * 10
        print('Персонаж восстановился после боя')

    def level_up(self):
        self.level += 1
        print('Персонаж достиг {} уровня'.format(self.level))

    def level_down(self):
        self.level -= 1
        print('Персонаж опустился до {} уровня'.format(self.level))

    def skills_up(self):
        print('У вас 3 очка для повышения характеристик персонажа')
        p, a, l = map(int, input('Увеличьте силу, ловкость и удачу: ').split(' '))
        while (p + a + l) != 3:
            p, a, l = map(int, input('Увеличьте силу, ловкость и удачу (у вас 3 очка): ').split(' '))
        self.power += p
        self.agility += a
        self.luck += l
        print('Сила увеличена на {}, ловкость на {}, удача на {}'.format(p, a, l))
        print('Обновленные характеристики: \nСила: {} \nЛовкость: {} \nУдача: {}'.format(self.power, self.agility, self.luck))
        self.refresh_skills()

    def refresh_skills(self):
        self.health = self.power * 10
        self.attack_speed = 60 / self.agility
        self.defence = self.agility * 5


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

        winner = character if total_time_character < total_time_monster else monster
        if winner is character:
            print('Персонаж победил')
            character.level_up()
            character.recover()
            character.skills_up()


c = Character(10, 10, 7)
m = Monster()
f = Fight()
f.start_the_fight(c, m)

