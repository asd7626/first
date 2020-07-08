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

    def level_up(self):
        self.level += 1
        print('Персонаж достиг {} уровня'.format(self.level))

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

    weapon_status = False

    def pick_weapon(self, other):
        if self.weapon_status == False:
            self.weapon_status = True
            self.power += other.power
            self.agility += other.agility
            self.luck += other.luck
            print('Персонаж подобрал одноручное оружие и получает'
                  ' +{} к силе и +{} к удаче. Ловкость уменьшиласа на {} пунктов'
                  .format(other.power, other.luck, other.agility))
        else:
            print('У персонажа уже есть оружие')
        print(self.power, self.agility, self.luck)
        self.refresh_skills()

    def drop_weapon(self, other):
        if self.weapon_status:
            self.power -= other.power
            self.agility -= other.agility
            self.luck -= other.luck
            self.weapon_status = False
            print('Персонаж выбросил одноручное оружие')
        else:
            print('У персонажа нет оружия')
        print(self.power, self.agility, self.luck)
        self.refresh_skills()


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

    def recover(self):
        self.health = self.power * 10


class Weapon:

    def __init__(self):
        self.power = 0
        self.agility = 0
        self.luck = 0


class OneHandedWeapon(Weapon):

    def __init__(self):
        super().__init__()
        self.power = 2
        self.agility = -2
        self.luck = 1


class TwoHandedWeapon(Weapon):

    def __init__(self):
        super().__init__()
        self.power = 4
        self.agility = -3
        self.luck = 2


class Fight:

    @staticmethod
    def start_the_fight(character, monster):
        character.recover()
        monster.recover()
        character_punch_count = 0
        monster_punch_count = 0
        print('Бой начался. У Игрока {} хп, у Монстра {} хп'.format(character.health, monster.health))
        while character.health > 0 or monster.health > 0:

            if monster.health > 0:
                character_punch_count += 1
            character.hit(monster)
            #print('Удар персонажа: ', character.punch)

            if character.health > 0:
                monster_punch_count += 1
            monster.hit(character)
            #print('Удар монстра: ', monster.punch)

        print('Кол-во ударов Персонажа: ', character_punch_count)
        print('Кол-во ударов Монстра: ', monster_punch_count)

        total_time_character = character_punch_count * character.attack_speed
        total_time_monster = monster_punch_count * monster.attack_speed
        print('Общее время Персонажа:' , total_time_character, 'секунд')
        print('Общее время Монстра:', total_time_monster, 'секунд')

        winner = character if total_time_character < total_time_monster else monster
        if winner is character:
            print('Персонаж победил')
            #character.level_up()
            #character.skills_up()


c = Character(10, 10, 7)
m = Monster()
f = Fight()
f.start_the_fight(c, m)
weapon1 = OneHandedWeapon()
weapon2 = TwoHandedWeapon()
c.pick_weapon(weapon2)
f.start_the_fight(c, m)

