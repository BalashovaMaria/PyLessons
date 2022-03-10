#1(2.1)
students = ["Вася", "Маша", "Петя", "Дима", "Марина", "Люба", "Коля", "Ваня"]
grades = {"Вася" : 4, "Петя" : 9, "Марина" : 8, "Люба" : 4, "Коля" : 5, "Ваня": 10}
for item in students:
    if item in grades:
        print('name of students', item, grades[item])
    else:
        print(item, 'ne pisal kr')

#2(2.2)
students = ["Вася", "Маша", "Петя", "Дима", "Марина", "Люба", "Коля", "Ваня"]
grades = {"Вася" : 4, "Петя" : 9, "Марина" : 8, "Люба" : 4, "Коля" : 5, "Ваня": 10}
for item in grades:
    if grades[item]>=8:
        print(item ,'otlichnik')

#3(2.3)
students = ["Вася", "Маша", "Петя", "Дима", "Марина", "Люба", "Коля", "Ваня"]
grades = {"Вася" : 4, "Петя" : 9, "Марина" : 8, "Люба" : 4, "Коля" : 5, "Ваня": 10}
good=[]
bad=[]
for item in students:
    if item in grades:
        if grades[item] >= 8:
            good.append(item)
        else:
            bad.append(item)
print('otlichniki:',good, 'norm:',bad)

#4(3)
marks = {'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
        'John' : [3, 3, 6, 8, 2, 1, 8, 5],
        'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
        'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]}
kyrs = int(input()) - 1
k=0
s=0
for item in marks:
    k=k+1;
    s=s+marks[item][kyrs];
print (f" оценка за {kyrs} курс равна {round(s/k)}")

#5(4)
marks = {'Mary': [5, 8, 9, 10, 3, 5, 6, 6],
'John': [3, 3, 6, 8, 2, 1, 8, 5],
'Alex': [4, 4, 7, 4, 7, 3, 2, 9],
'Patricia': [2, 1, 6, 8, 2, 3, 7, 4]}
categories = {'отлично': [8, 9, 10],
'хорошо': [6, 7],
'удовлетворительно': [4, 5],
'неуд': [0, 1, 2, 3]}
kyrs = int(input('vvedite kyrs:')) - 1
total = 0
for item in marks.values():
    total += item[kyrs]
for i, m in categories.items():
    if round(total / len(marks)) in m:
        print(i)
        
#6(5)
marks = {'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
        'John' : [3, 3, 6, 8, 2, 1, 8, 5],
        'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
        'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]}
ocenka=int(input('vvedite ocenky'))
nach=0
for k, v in marks.items():
    for el in v:
        if el>=ocenka:
            nach+=1
print (nach)

#7(34)
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]
s = {}

for query in queries:
    words = query.split()

    if len(words) in s.keys():
        s[len(words)] += 1
    else:
        s.update({
            len(words): 1
        })

for key, value in s.items():
    percent = round((value / len(queries)) * 100, 2)
    print(f'Поисковых запросов, содержащих {key} слов(a): {percent}% ')
    
