import os
import json
import re
import creature
from rich.console import Console

console = Console()

class InvalidJsonData(Exception):
    def __init__(self, message = "Не корректный формат данных") -> None:
        self.message = message
        super().__init__(self.message)


def check_json(json_dict):

    json_str = json.dumps(json_dict)
    pat = r'^\{"player_hp": \d+, "monster_hp": \d+, "turn": \d+\}$'
    if not re.match(pat, json_str):
        raise InvalidJsonData("Файл сохраниния должен быть в формате: {'player_hp': <число>, 'monster_hp': <число>, 'turn': <число>}")

def save(player, monster, turn):
    save_data ={}
    
    save_data["player_hp"] = player.hp
    save_data["monster_hp"] = monster.hp
    save_data["turn"] = turn

    with open("save.json", "w") as save_file:
        json.dump(save_data, save_file)

def load():

    player = creature.Player()
    monster = creature.Monster()
    turn = 1

    def incorrect_file():
        ans = input("Файл сохранения не корректен! Удалить? (да/нет)").lower()
        if ans == "да":
            os.remove("save.json")
            save(player, monster, turn)
        else:
            exit()

    if os.path.exists("save.json"):
        ans = input("Обнаружен файл сохранения. Хотите начать играть с него(да/нет)").lower()

        if ans == "нет":
            save(creature.Player(), creature.Monster(), 1)

    try:
        with open("save.json", "r") as save_file:
            save_data = json.load(save_file)
            check_json(save_data)

            player.hp = save_data["player_hp"]
            monster.hp = save_data["monster_hp"]
            turn = save_data["turn"]


    except FileNotFoundError:
        console.print("Файл сохранения не существует и будет создан автоматически!")
        save(creature.Player(), creature.Monster(), turn)
    except json.JSONDecodeError:
        incorrect_file()
    except InvalidJsonData as e:
        console.print(e)
        incorrect_file()

    return [player, monster, turn]

