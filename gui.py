from rich.table import Table
from rich.console import Console

console = Console()


def draw_table(player, monster, turn):
    table = Table(title=f"Ход:{turn}")
    table.add_column("Боец")
    table.add_column("Выбор")
    table.add_column("Защита")
    table.add_column("Сила атаки")
    table.add_column("Здоровье")

    table.add_row(player.name, player.choice, str(player.defense), str(player.attack_power), str(player.hp))
    table.add_row(monster.name, monster.choice, str(monster.defense), str(monster.attack_power), str(monster.hp))


    console.print(table)
