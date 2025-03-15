import time
import random
from colorama import Fore
import json
import os
import re
import pdb

class InvalidJsonData(Exception):
    def __init__(self, message = "Не корректный формат данных") -> None:
        self.message = message
        super().__init__(self.message)

print("Добро пожаловать в игру про драки с монстром!")

player_hp = 100
monster_hp = 100
turn = 1

varians = ["защита", "атака"]

delay = 1

def player_choise():# Выбор тактики игроком
    p_ch = ""
    while True:
        p_ch = input("Что ты выберешь(защита/атака)? 'в' - выход\n>>>").lower() 
        if p_ch == "в":
            exit()
        if p_ch not in varians:
            print("Такого варианта нет!")
        else:
            print(f"Ты выбрал {p_ch}")
            time.sleep(delay)
            return p_ch


def monster_choise():# Генерация тактики монстра
    m_ch = random.choice(varians)
    print(f"Монстр выбрал {m_ch}")
    return m_ch

def print_hp():# Вывод показателей здоровья
    print(f"Здоровье игрока {player_hp}")
    print(f"Здоровье монстра {monster_hp}")

def attack(choise_1, choise_2, subject_name):# Просчет результата атаки
    
    s_dam = random.randint(0, 10)
    e_arm = random.randint(0, 10)

    if choise_1 == "атака": 
        if choise_2 == "защита":
            print(f"{"Монстр" if subject_name == "Игрок" else "Игрок"} защищается. Броня: {e_arm}")
            s_dam = max(0, s_dam - e_arm)
        
        if subject_name == "Игрок":
            global monster_hp
            monster_hp -= s_dam
        else:
            global player_hp
            player_hp -= s_dam
        print(f"{subject_name} наносит {s_dam} урона")
        time.sleep(delay)
    elif choise_2 == "защита" and subject_name == "Монстр":
        print("Два дурачка стоят и защищаются! Ахахахах!")

def check_json(json_dict):

    json_str = json.dumps(json_dict)
    pat = r'^\{"player_hp": \d+, "monster_hp": \d+, "turn": \d+\}$'
    if not re.match(pat, json_str):
        raise InvalidJsonData("Файл сохраниния должен быть в формате: {'player_hp': <число>, 'monster_hp': <число>, 'turn': <число>}")

def save():
    save_data ={}
    
    global player_hp
    global monster_hp
    global turn


    save_data["player_hp"] = player_hp
    save_data["monster_hp"] = monster_hp
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

            global player_hp
            global monster_hp
            global turn

            player_hp = save_data["player_hp"]
            monster_hp = save_data["monster_hp"]
            turn = save_data["turn"]


    except FileNotFoundError:
        print("Файл сохранения не существует и будет создан автоматически!")
        save()
    except json.JSONDecodeError:
        incorrect_file()
    except InvalidJsonData as e:
        print(e)
        incorrect_file()
 
#player_hp = 10
#monster_hp = 10

load()

while True:
    if monster_hp <= 0 or player_hp <= 0:
        break

    print_hp()
    print(f"Ход номер:{turn}")

    p_ch = player_choise()
    m_ch = monster_choise()

    attack(p_ch, m_ch, "Игрок")
    attack(m_ch, p_ch, "Монстр")

    turn += 1

    save()


if player_hp <= 0 and monster_hp <= 0:
    print(Fore.RED + "Погибли оба!" + Fore.RESET)
elif player_hp <= 0:
    print(Fore.RED + "Вы погибли!" + Fore.RESET)
else:
    print(Fore.GREEN + "Вы победили" + Fore.RESET)

input("Для выхода нажмите ENTER")
