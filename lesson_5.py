'''
Занятие 5.
К сожалению не смог зайти на стрим. Но банальное, как казалось, задание оказалось интересным. Полученые навыки мне пригодятся.
'''
from collections import defaultdict

#songs =   "Yesterday, Bohemian Rhapsody, Imagine, Hotel California, We Will Rock You, Stairway to Heaven, Smells Like Teen Spirit, Hey Jude, Thriller, Like a Rolling Stone, Purple Haze, Billie Jean, Let It Be, Sweet Child o' Mine, Dancing Queen, Hallelujah, Wonderwall, Shape of You, Rolling in the Deep, Fix You"

#artists = "The Beatles, Queen, John Lennon, Eagles, Queen, Led Zeppelin, Nirvana, The Beatles, Michael Jackson, Bob Dylan, Jimi Hendrix, Michael Jackson, The Beatles, Guns N' Roses, ABBA, Leonard Cohen, Oasis, Ed Sheeran, Adele, Coldplay"
#Я тестировал на данных из этих пременных. Решил их оставить. Вдруг пригодятся.

songs = input("Введите список песен разделенных запятой.\n>>>")
artists = input("Введите список испольнителей разделенных запятой\n>>>")

songs = songs.split(',')
artists = artists.split(',')

songs = [x.lstrip() for x in songs] #  Надо удалить лишние пробелы. Иначе будет неудобно.
artists = [x.lstrip() for x in artists]

dict_songs = {}

if len(artists) != len(songs): # Ситуация когда строки не совпадают по размеру. Надо предупредить пользователя что часть данных пропала. Но это не критично и программа продолжит работать.
    print("Предупреждение: списки имеют разное количество элементов и часть данных будет потеряна!")

if len(artists) == 0 or len(songs) == 0: # Но пустые строки это недопустимый вариант. Программа переходит к выполнению последней строки. Думал написать функцию для обработки ситуаций. Но мы их, вроде, не проходили.
    print("Ошибка. Использование пустых строк недопустимо.")
else:

    print("Плейлист:")
    for i, (artist, song) in enumerate(zip(artists, songs)): # zip нельзя присвоить переменной. Я использовал его несколько раз. Возможно стоило привести его к списку. Но пока не знаю как это работает. Оставил так.
        print(f"    {i + 1}. {song} - {artist}")
    
    dict_songs = defaultdict(list) # узнал о такой интересной штуке. Можно не проверять на наличие ключа. Сразу решил применить.

    print("\nГруппировака по исполнителям:")

    for key, value in zip(artists, songs):
        dict_songs[key.lower()].append((key, value)) # Пользователь может написать название группы с маленькой буквы. Но это не должно влиять на порядок группироваки.
        
    for key in dict_songs.keys(): # Вывод я тоже решил сделать похожим на вывод плейлиста. Название группы мы берем из первого ввода, а не из ключа. Ну и каждую песню группы мы пронумеруем.
        print(f"    {dict_songs[key][0][0]}")
        for i, song in enumerate(dict_songs[key]):
            print(f"        {i + 1}. {song[1]}")



input("\nНажмите ENTER чтобы выйти.")
