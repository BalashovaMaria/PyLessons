import re
txt = open("students.txt",  encoding="utf8")
lst = txt.read().split("\n")
sort=lst.sort()

def add():
    student = input('Введите фамилию и имя нового студента: ')
    if student in lst:
        print(student, 'уже есть в списке')
    else:
        lst.append(student)
        lst.sort()
        print(student, 'добавлен(а)')

def find():
    surname = input('Введите фамилию студента: ')
    name = input('Введите имя студента или пропустите этот параметр: ')
    stud=surname+ " " + name
    if name == '':
        for i in lst:
            if surname in i:
                sur=re.findall(r'\w+', i)[0]
                if surname == sur:
                    print('Студент с этой фамилией: ',i )
                else:
                    print('Такого студента нет в списке')
    else:
        if stud in lst:
            print('Студент находится в группе')
        else:
            print('Студент не находится в группе')

def edit():
    surname = input('Введите фамилию студента: ')
    name = input('Введите имя студента: ')
    stud = surname + " " + name
    if stud in lst:
        for i in lst:
            if stud == i:
                print('Что вы хотите поменять?(имя,фамилия или имя и фамилия)')
                answer = input()
                if answer == 'имя':
                    new_name = input('Введите новое имя студента: ')
                    lst.remove(stud)
                    app = surname + " " + new_name
                    lst.append(app)
                    lst.sort()
                    print('Имя студента изменено')
                elif answer == 'фамилия':
                    new_surname = input('Введите новую фамилию студента: ')
                    lst.remove(stud)
                    app = new_surname + " " + name
                    lst.append(app)
                    lst.sort()
                    print('Фамилия студента изменена')
                elif answer == 'имя и фамилия':
                    new_name = input('Введите новое имя студента: ')
                    new_surname = input('Введите новую фамилию студента: ')
                    lst.remove(stud)
                    app = new_surname + " " + new_name
                    lst.append(app)
                    lst.sort()
                    print('Имя и фамилия студента изменены')
    else:
        print('Такого студента нет в списке')

def remove():
    surname = input('Введите фамилию студента: ')
    name = input('Введите имя студента или пропустите этот параметр: ')
    stud = surname + " " + name
    if name == '':
        for i in lst:
            if surname in i:
                sur = re.findall(r'\w+', i)[0]
                if surname == sur:
                    print('Студенты с этой фамилией: ', i, 'и' ,i)
                nname = input('Введите имя студента: ')
                student = surname + " " + nname
                if student in lst:
                    lst.remove(student)
                    lst.sort()
                    print('Студент удален')
    else:
        if stud in lst:
            for i in lst:
                if stud == i:
                    lst.remove(stud)
                    lst.sort()
                    print('Студент удален')
        else:
            print('Такого студента нет в списке')

while (True):
    command = input('Введите команду(add,find,edit,remove,end): ')
    if command == 'add':
        add()
    if command == 'find':
        find()
    if command == 'edit':
        edit()
    if command == 'remove':
        remove()
    if command == 'end':
        break
