#задание 5
import random

words = ['самовар', 'весна', 'лето']
word = random.choice(words)
nomer = random.randint(0, len(word) - 1)
for x in range(len(word)):
    if x==nomer:
        print('?',end='')
        continue
    print(word[x],end='')
print(' ')
if True:
    f = input('\nВведите букву:')
    if f == word[nomer]:
        print(f'Победа! \nСлово :{word}')
    else:
        print(f'Увы! Попробуйте в другой раз\nСлово:{word}')
#Задание 6
text = '''В тот год осенняя погода
Стояла долго на дворе
Зимы ждала ждала природа
Снег выпал только в январе
На третье в ночь Проснувшись рано
В окно увидела Татьяна
Поутру побелевший двор
Куртины, кровли и забор
На стеклах легкие узоры
Деревья в зимнем серебре
Сорок веселых на дворе
И мягко устланные горы
Зимы блистательным ковром
Все ярко, все бело кругом'''
stroki = text.count('\n')
print(f"строк {stroki+1}")
slova = len(text.split())
print(f"слов {slova}")
