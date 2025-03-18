'''
Урок 9. Использование ООП.
Переписал программу. Доработал то где ошибался. Наделал кучу новых ошибок. В общем, весело.
'''
from rich.console import Console
import gui
import data
import creature
console = Console()


        
console.print(f"[green]{creature.GameConstants.START_GAME_MESSEGE}[/green]")

player = creature.Player()
monster = creature.Monster()


turn = 1

player, monster, turn = data.load()

while player.hp > 0 and monster.hp > 0:


    gui.draw_table(player, monster, turn)

    player.do_choice()
    monster.do_choice()

    player.attack(monster)
    monster.attack(player)

    turn += 1

    data.save(player, monster, turn)

else:
    if monster.hp <= 0 and player.hp <= 0:
        console.print(f"[red]Умерли оба![/red]")
    elif player.hp > 0:
        console.print(f"[green]Победил {GameConstants.PLAYER_NAME}[/green]")
    elif monster.hp > 0:
        console.print(f"[red]Победил {GameConstants.MONSTER_NAME}[/red]")

input("Для выхода нажмите Enter...")
