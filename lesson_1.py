""" 
Первый урок. 
Решил не придумывать своего. Просто переделать так как сделал бы я в какой-нибудь своей программе.
"""
list_of_keys = ["имя", "возраст", "цвет", "существительное", "глагол"]

items = {key: input(f"Введите {key}\n>>>") for key in list_of_keys}


print(f"Привет! Меня зовут {items['имя']}.")
print(f"Мой возраст {items['возраст']} лет.")
print(f"{items['цвет'].capitalize()} {items['существительное']} {items['глагол']} меня по голове!")
input("Нажмите Enter для выхода...")
