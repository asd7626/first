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
        self.refresh_health()
        self.refresh_attack_speed()

    def recover(self, x):
        self.health = 0
        self.health += x

    def refresh_health(self):
        self.health = self.power * 10

    def refresh_attack_speed(self):
        self.attack_speed = 60 / self.agility

    sword = None
    helmet = None
    armor = None
    boots = None

    def pick_item(self, item):
        if item.kind == 'Sword':
            if self.sword is None:
                self.sword = True
                self.power = self.power + math.floor(item.power * (self.luck/10))
                self.agility = self.agility + item.agility
                self.refresh_health()
                self.refresh_attack_speed()
                print('Персонаж подобрал меч')
            else:
                print('У персонажа уже есть меч!')
        elif item.kind == 'Helmet':
            if self.helmet is None:
                self.helmet = True
                self.health = self.health + math.floor(item.health * (self.luck/10))
                print('Персонаж подобрал шлем')
            else:
                print('У персонажа уже есть шлем!')
        elif item.kind == 'Armor':
            if self.armor is None:
                self.armor = True
                self.agility = self.agility + item.agility
                self.refresh_attack_speed()
                self.health = self.health + math.floor(item.health * (self.luck/10))
                print('Персонаж подобрал броню')
            else:
                print('У персонажа уже есть броня!')
        elif item.kind == 'Boots':
            if self.boots is None:
                self.boots = True
                self.agility = self.agility + item.agility
                self.refresh_attack_speed()
                self.health = self.health + math.floor(item.health * (self.luck/10))
                print('Персонаж подобрал обувь')
            else:
                print('У персонажа уже есть обувь!')

    def drop_item(self, item):

        if item.kind == 'Sword':
            if self.sword is True:
                self.sword = None
                self.power = self.power - math.floor(item.power * (self.luck/10))
                self.agility = self.agility - item.agility
                self.refresh_health()
                self.refresh_attack_speed()
                print('Персонаж выбросил меч')
            else:
                print('У персонажа нет оружия!')

        elif item.kind == 'Helmet':
            if self.helmet is True:
                self.helmet = None
                self.health = self.health - math.floor(item.health * (self.luck/10))
                print('Персонаж выбросил шлем')
            else:
                print('У персонажа нет шлема!')

        elif item.kind == 'Armor':
            if self.armor is True:
                self.armor = None
                self.agility = self.agility - item.agility
                self.refresh_attack_speed()
                self.health = self.health - math.floor(item.health * (self.luck/10))
                print('Персонаж выбросил броню')
            else:
                print('У персонажа нет брони!')

        elif item.kind == 'Boots':
            if self.boots is True:
                self.boots = None
                self.agility = self.agility - item.agility
                self.refresh_attack_speed()
                self.health = self.health - math.floor(item.health * (self.luck/10))
                print('Персонаж выбросил обувь')
            else:
                print('У персонажа нет обуви!')

    def characteristics(self):
        return 'Характеристики Персонажа: \n' \
               'Сила: {};' \
               ' Ловкость: {};'\
               ' Удача: {};'\
               ' Здоровье: {};' \
               ' Скорость атаки: {};' \
               .format(self.power, self.agility, self.luck, self.health, self.attack_speed)


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

    def refresh_health(self):
        self.health = self.power * 10


class Item:

    def __init__(self, kind):
        #self.items = ('Sword', 'Helmet', 'Armor', 'Boots')
        #self.kind = random.choice(self.items)
        self.kind = kind
        print(self.kind + ' создан')
        self.characteristics()

    def characteristics(self):
        if self.kind == 'Sword':
            self.power = random.randrange(2, 10, 1)
            self.agility = -1
            self.health = 0
        elif self.kind == 'Helmet':
            self.health = random.randrange(10, 20, 1)
            self.power = 0
            self.agility = 0
        elif self.kind == 'Armor':
            self.agility = -2
            self.health = random.randrange(20, 30, 1)
            self.power = 0
        elif self.kind == 'Boots':
            self.agility = 1
            self.health = random.randrange(10, 20, 1)
            self.power = 0


class Fight:

    @staticmethod
    def start_the_fight(character, monster):
        health_to_recover = character.health
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
        character.recover(health_to_recover)
        monster.refresh_health()
        offer_chance = random.randrange(1, 5)
        if winner is character:
            print('Персонаж победил')
            #character.level_up()
            #character.skills_up()
            #if offer_chance < 2:
            #f.offer_item(character, item1)
            #else: pass

    @staticmethod
    def offer_item(character, itm):
        print('Игроку выпал {} со следующими характеристиками:\n'
              'Сила: {}, Ловкость: {} и Здоровье: {:.0f} хп.'
              ' Хотите надеть этот предмет?'.format(itm.kind, math.floor(itm.power*(character.luck/10)),
                itm.agility, math.floor(itm.health*(character.luck/10))))
        yes_no_input = int(input('1 - Да. 2 - Нет: '))
        if yes_no_input == 1:
            character.pick_item(itm)
            print('Персонаж подобрал {}. Ваши обновленные характеристики:'
                  ' Сила: {}, Ловкость: {}, Здоровье: {}'.format(itm.kind, character.power, character.agility,
                    character.health))
        else:
            print('Игрок отказался от предмета. Характеристики остались неизменными.')


c = Character(10, 10, 7)
m = Monster()
sword = Item('Sword')
armor = Item('Armor')
helmet = Item('Helmet')
boots = Item('Boots')


