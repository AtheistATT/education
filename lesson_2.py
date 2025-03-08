""" 
Второй урок. 
Решил использовать тот же способ вводы что и в первой программе. Перемудрил конечно. Но зато проще добавить новый ингридиент.
"""
list_of_ingr= ["трава", "кристалы", "вода", "огненная пыль", "лунный свет"]
power_sets = [0.5, 1.5, 0.8, 1.0, 1.2]


items = {key: float(input(f"Введите значение ингридиента '{key}' \n>>>")) for key in list_of_ingr}

magic_power = sum([items[x] * power_sets[i] for i, x in enumerate(list_of_ingr)]) 


count_items = sum(items.values())

magic_power += 20 * (count_items > 150)

print(f"Вы приготовили зелье мощностью {magic_power} чаров.")
input("Нажмите Enter для выхода...")
