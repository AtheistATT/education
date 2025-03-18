from rich import console
from rich.console import Console
import random
console = Console()
class GameConstants(): # Вынес все константы в отдельный класс чтобы избежать ошибок
    ATTACK = "Атака"
    DEFENSE = "Защита"
    MAX_DEFENSE = 10
    MAX_ATTACK = 10
    MAX_HP = 125
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
        enemy.take_demage(self.attack_power)
 
    def take_demage(self, amound):
        self.hp -= max(0, amound - self.defense)   

    def display_helth(self):
        return f"{self.hp}({int(self.hp/ GameConstants.MAX_HP * 100)}%)"

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
