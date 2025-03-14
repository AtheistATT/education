import time
import random
from colorama import Fore

print("Добро пожаловать в игру про драки с монстром!")

player_hp = 100
monster_hp = 100

varians = ["защита", "атака"]

delay = 1

def player_choise():# Выбор тактики игроком
    p_ch = ""
    while True:
        p_ch = input("Что ты выберешь(защита/атака)?").lower() 
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
player_hp = 10
monster_hp = 10

while True:
    if monster_hp <= 0 or player_hp <= 0:
        break

    print_hp()

    p_ch = player_choise()
    m_ch = monster_choise()

    attack(p_ch, m_ch, "Игрок")
    attack(m_ch, p_ch, "Монстр")

if player_hp <= 0 and monster_hp <= 0:
    print(Fore.RED + "Погибли оба!" + Fore.RESET)
elif player_hp <= 0:
    print(Fore.RED + "Вы погибли!" + Fore.RESET)
else:
    print(Fore.GREEN + "Вы победили" + Fore.RESET)

input("Для выхода нажмите ENTER")
