'''
Урок 9. Использование ООП.
Переписал программу. Доработал то где ошибался. Наделал кучу новых ошибок. В общем, весело.
'''
import random
#import pdb
from inquirer.render import console
from rich import table
from rich.console import Console
from rich.table import Table
import os
import json
import re

console = Console()

class InvalidJsonData(Exception):
    def __init__(self, message = "Не корректный формат данных") -> None:
        self.message = message
        super().__init__(self.message)

class GameConstants(): # Вынес все константы в отдельный класс чтобы избежать ошибок
    ATTACK = "Атака"
    DEFENSE = "Защита"
    MAX_DEFENSE = 10
    MAX_ATTACK = 10
    MAX_HP = 100
    MONSTER_NAME = "Монстр"
    PLAYER_NAME = "Игрок"
    MESSAGE_CHOICE = "Выберете свою стратегию (Атака/Защита/Выход)"
    START_GAME_MESSEGE = "Добро пожаловать в игру про сражение с монстром"

class Creature(): # Базовый класс для игрока и монстра
    def __init__(self) -> None:
        self.hp = GameConstants.MAX_HP
        self.defense = 0
        self.name = ""
        self.choice = ""
        self.attack_power = 0

    def get_defence(self):
        if self.choice == GameConstants.ATTACK:
            self.defense = 0
            return
        self.defense = random.randint(0, GameConstants.MAX_DEFENSE)
        self.attack_power = 0

    def attack(self, enemy):
        self.attack_power = random.randint(0, GameConstants.MAX_ATTACK) if self.choice == GameConstants.ATTACK else 0
        enemy.hp -= max(0, self.attack_power - enemy.defense)

#    def test(self):# Вывод данных нужен исключительно для тестирования
#        print(f"hp:{self.hp}")
#        print(f"defense:{self.defense}")
#        print(f"name:{self.name}")
#        print(f"choice:{self.choice}")
#        print(f"attack_power:{self.attack_power}")

class Monster(Creature):# Класс монстра
    def __init__(self) -> None:
        super().__init__()
        self.name = GameConstants.MONSTER_NAME

    def do_choice(self):
        self.choice = random.choice((GameConstants.ATTACK, GameConstants.DEFENSE))
        super().get_defence()

class Player(Creature):# Класс игрока
    def __init__(self) -> None:
        super().__init__()
        self.name = GameConstants.PLAYER_NAME

    def do_choice(self):

        self.choice = ''

        options = [GameConstants.ATTACK, GameConstants.DEFENSE, "Выход"] 
        while self.choice not in options:
            p_choice = console.input(f"[green]{GameConstants.MESSAGE_CHOICE}\n>>>[/green]").capitalize() 
            self.choice = p_choice
            
            if p_choice not in options:
                console.print("Такого варианта нет")

        if p_choice == "Выход":
            exit()

        super().get_defence()
        
def check_json(json_dict):

    json_str = json.dumps(json_dict)
    pat = r'^\{"player_hp": \d+, "monster_hp": \d+, "turn": \d+\}$'
    if not re.match(pat, json_str):
        raise InvalidJsonData("Файл сохраниния должен быть в формате: {'player_hp': <число>, 'monster_hp': <число>, 'turn': <число>}")

def save():
    save_data ={}
    
    save_data["player_hp"] = player.hp
    save_data["monster_hp"] = monster.hp
    save_data["turn"] = turn

    with open("save.json", "w") as save_file:
        json.dump(save_data, save_file)

def load():

    def incorrect_file():
        ans = input("Файл сохранения не корректен! Удалить? (да/нет)").lower()
        if ans == "да":
            os.remove("save.json")
            save()
        else:
            exit()

    if os.path.exists("save.json"):
        ans = input("Обнаружен файл сохранения. Хотите начать играть с него(да/нет)").lower()

        if ans == "нет":
            save()

    try:
        with open("save.json", "r") as save_file:
            save_data = json.load(save_file)
            check_json(save_data)

            player.hp = save_data["player_hp"]
            monster.hp = save_data["monster_hp"]
            global turn
            turn = save_data["turn"]


    except FileNotFoundError:
        console.print("Файл сохранения не существует и будет создан автоматически!")
        save()
    except json.JSONDecodeError:
        incorrect_file()
    except InvalidJsonData as e:
        console.print(e)
        incorrect_file()

console.print(f"[green]{GameConstants.START_GAME_MESSEGE}[/green]")

player = Player()
monster = Monster()


turn = 1

load()

while player.hp > 0 and monster.hp > 0:

    table = Table(title=f"Ход:{turn}")
    table.add_column("Боец")
    table.add_column("Выбор")
    table.add_column("Защита")
    table.add_column("Сила атаки")
    table.add_column("Здоровье")

    table.add_row(player.name, player.choice, str(player.defense), str(player.attack_power), str(player.hp))
    table.add_row(monster.name, monster.choice, str(monster.defense), str(monster.attack_power), str(monster.hp))


    console.print(table)

    player.do_choice()
    monster.do_choice()

    player.attack(monster)
    monster.attack(player)

    turn += 1

    save()

else:
    if monster.hp <= 0 and player.hp <= 0:
        console.print(f"[red]Умерли оба![/red]")
    elif player.hp > 0:
        console.print(f"[green]Победил {GameConstants.PLAYER_NAME}[/green]")
    elif monster.hp > 0:
        console.print(f"[red]Победил {GameConstants.MONSTER_NAME}[/red]")

input("Для выхода нажмите Enter...")
