'''
Домашнее задание №6.

В этом задании я решил проявить творчество. Реализаций игры может быть много. Я решил что органичнее всего тут реализовать используя ООП. Так как и монстра и игрока проще представить объектом. Кроме того и у того и у другого есть одинаковые характеристики и методы. Я использовал наследования. Опыт ООП в пайтоне у меня недольшой. Но, вроде, все работает
'''
import time
import random
from colorama import Fore
#import pdb
import inquirer

class Essence: # Класс сущности. Содержит общие характеристики как игрока так и монстра
    def __init__(self) -> None:
        self.hp = 0
        self.max_damage = 0
        self.protect = 0
        self.ch = ''
        self.rez = ''
        self.name = ''

    def damage(self, enemy):# Метод который вызывается в случе если соблюдены условия получения урона противником
        prot = random.randint(1, 5)
        dam = random.randint(5, self.max_damage)
        
        if enemy.protect > prot:
            enemy.protect -= prot
        else:
            prot = enemy.protect
            enemy.protect = 0

        dam = max(0, dam - prot)
        
        enemy.hp -= dam

        print(f"{self.me} наносит урон - {dam - prot}")


    def hit(self, enemy): # Общий метод логики атаки. Наследуется как игроком так и монстром.
        if self.ch == "Защищаться":
            print(f"{self.me} защищается.")
            return
        else:
            if enemy.ch == "Атаковать":
                if self.rez == "Удача":
                        self.damage(enemy)
                else:
                    print(f"{self.me} промахивается.")
            else:
                if enemy.rez == "Неудача":
                    self.damage(enemy)
                else:
                    print(f"{enemy.me} блокирует атаку")
           # pdb.set_trace()

class Monster(Essence):
    #   Списки монстров и их характеристик
    type_monster_list = [("Слизняк", 25), ("Гоблин", 50), ("Зомби", 75), ("Орк", 100), ("Тролль", 150), ("Энт", 200), ("Дракон", 300)]
    strong_list = (("Умиращий", 0.25), ("Больной", 0.50), ("Слабый", 0.75), ("Обычный", 1), ("Крепкий", 1.25), ("Опытный", 1.50), ("Матерый", 1.75), ("Легендарный", 2))
    behavior_list = ("Трусливый", "Осторожный", "Разумный", "Злой", "Яростный")


    def __init__(self) -> None:# При инициализации генерируется случайный монстр. Имя состоит из 3 слов <Стратегия> <Сила> <Тип монстра>. 
        self.current_monster = []
        self.current_monster.append(random.choice(self.behavior_list))
        self.current_monster.append(random.choice(self.strong_list))
        self.current_monster.append(random.choice(self.type_monster_list))
        self.me = "Монстр"

        monster = [self.current_monster[0], self.current_monster[1][0], self.current_monster[2][0]]

        def_hp = self.current_monster[2][1]
        strong = self.current_monster[1][1]

        print(Fore.RED + "Против вас сражается {} {} {}".format(*monster) +Fore.RESET )

        # Вычисляем здоровье и урон
        self.hp =  round(def_hp * strong)
        self.max_damage = round(def_hp / 5 * strong)
        self.protect =  round(def_hp / 2)
        self.me = "Монстр"

    def choise(self):# Выбор монстра. Вероятность выбора зависит от его стратегии. На стратегию указывает первое слово
        behavior = self.current_monster[0]
        ch = ''

        match(behavior):
            case "Трусливый":
                ch = "Атаковать" if random.randint(1,6) == 1 else "Защищаться"
                print(f"Монстр выбрал стратегию - {ch}")
            case "Осторожный":
                ch = "Атаковать" if random.randint(1,6) <= 2 else "Защищаться"
                print(f"Монстр выбрал стратегию - {ch}")
            case "Разумный":
                ch = "Атаковать" if random.randint(1,6) <= 3 else "Защищаться"
                print(f"Монстр выбрал стратегию - {ch}")
            case "Злой":
                ch = "Атаковать" if random.randint(1,6) <= 4 else "Защищаться"
                print(f"Монстр выбрал стратегию - {ch}")
            case "Яростный":
                ch = "Атаковать" if random.randint(1,6) <= 5 else "Защищаться"
                print(f"Монстр выбрал стратегию - {ch}")

        rez = "Неудача" if random.randint(1,3) == 1 else "Удача"
        print(f"Результат - {rez}")

        self.ch = ch
        self.rez = rez

    def hit(self, enemy):
        return super().hit(enemy)



class Player(Essence):
    def __init__(self) -> None:
        input("Давайте бросим кости чтобы определить ваши характеристики. Нажмите Enter.")
        time.sleep(1)

        self.hp = 50 + random.randint(1,35) * 10
        self.max_damage = 10 + random.randint(1,35) * 2
        self.protect = round(self.hp / 2)
        self.me = "Игрок"
        print(f"Ваше Здоровье:{self.hp}\nВаша сила:{self.max_damage}\nВаша защита: {self.protect}")

    def choise(self):# Выбор игрока. Для выбора я использовал inquirer. Так гораздо удобнее.
        question = [inquirer.List("do", message="Что делать?", choices=["Атаковать", "Защищаться"])]
        ansver = inquirer.prompt(question)

        ch = ansver["do"]
        print(f"Вы выбрали - {ch}")

        rez = "Неудача" if random.randint(1, 3) == 1 else "Удача"
        print(f"Результат - {rez}")
        
        self.ch = ch
        self.rez = rez

    def hit(self, enemy):
        return super().hit(enemy)




print("Добро пожаловать в пошаговый консольный файтинг - Охотник на монстров")

player = Player()
monster = Monster()


while player.hp > 0 and monster.hp > 0: # Основной цикл игры. Тут ничего интересного уже не происходит.
    
    player.choise()
    monster.choise()

    player.hit(monster)
    monster.hit(player)

    print(f"Игрок здоровье/защита {player.hp}/{player.protect}")
    print(f"Монстр здоровье/защита {monster.hp}/{monster.protect}")

else:
    if monster.hp <= 0:
        print(Fore.GREEN + "Вы победили." + Fore.RESET)
    else:
        print(Fore.RED + "Вы проиграли" + Fore.RESET)


#pdb.set_trace() # Код на случай если понадобится отладка я предпочитаю не удалять.


input("Нажмите Enter для выхода ...")
