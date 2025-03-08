'''
Урок 3.
Решение не самое оригинальное. Думаю можно и красивее. Но работает.
'''
input_string = input("Введите строку 'данные о продажах' в формате '<Товар1>:<Продано шт.>,<Товар2>:<Продано шт>' ...\n>>>")
input_string = input_string.replace(' ', '') 
input_string = input_string.lower() # Добавил удаление лишних пробелов и игнорирование регистра
                                         # Можно было еще добавить проверку на корректность по регуляркам
raw_list = [(y.split(':')[0], int(y.split(':')[1])) for y in input_string.split(',')]

dict_list = {}

for x in raw_list:
    if x[0] in dict_list:
        dict_list[x[0]] += x[1]
    else:
        dict_list[x[0]] = x[1]
print(dict_list)
for key, val in dict_list.items():
    print(f"Товар:'{key}' - Продано:'{val}' шт.")

input()
