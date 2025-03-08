'''
Урок 4.
Задание не такое веселое. Но я постарался добавить юмора.
'''
cost = input("Введите сумму покупки в фантиках\n>>>")
try:
    cost = int(cost)
except:
    print("Ваша валюта не может быть коррекно конвертирована в фантики!")
    print('Ok!')
    input()
    exit()

vip = input("Вы вип клиент? y(да)/n(нет)\n>>>").lower()
if vip not in ('y', 'n'):
    print("Нам не удалось корректно определить ваш статус. Ответы путаны. Может придете в другой раз?")
    print('Ok!')
    input()
    exit()

dis = 0

if cost > 1000:
    if vip == 'y':
        cost *= 0.75
        dis = 25
    else:
        cost *= 0.80
        dis = 20
elif cost > 500:
    cost *= 0.90
    dis = 10
elif cost >= 0:
    pass
else:
    if vip == 'y':
        if(cost > -1001):
            print("Мы готовы пойти вам навстречу и продать товар в кредит.")
        else:
            print("Даже статус вип клиента не позволяет вам просить так много.")
            print("ok!")
            input()
            exit()
    else:
        print("Как ты смеешь просить у меня денег?")
        print("ok!")
        input()
        exit()

print(f"Сумма покупки {cost}.\nВаша скидка составляет {dis}%.")

input("Ok!")


