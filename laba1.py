documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}

def polki():
    lst=[]
    lst2=[]
    for key in directories:
        lst.append(key)
    lst2=", ".join(lst)
    return (lst2)

'''1'''

def p(number_vl):
    for number_doc in documents:
        if number_doc['number'] == number_vl:
            print('Владелец документа: ', number_doc['name'])
            break
    else:
        print('Документ не найден в базе')

'''2'''

def s(number_polka):
    break_polka = False
    for polka_directory in directories.items():
        for number_doc in polka_directory[1]:
            if number_doc == number_polka:
                print('Документ хранится на полке: ', polka_directory[0])
                break_polka = True
                break
        if break_polka == True:
            break
    else:
        print('Документ не найден в базе')

'''3'''

def get_key(d, value):
 for k, v in d.items():
  if value in v:
   return k

def l():
 for c in documents:
  doc_type = c['type']
  number = c['number']
  name = c['name']
  print('№: {1}, тип: {0}, владелец: {2}, полка хранения: {3}'.format(doc_type, number, name, get_key(directories, number)))


'''4'''

def ads(new_polka):
    if int(new_polka) == 1 or int(new_polka) == 2 or int(new_polka) == 3:
        print('Такая полка уже существует. Текущий перечень полок: ', polki())
    else:
        new_directorie = {new_polka: []}
        directories.update(new_directorie)
        print('Полка добавлена.Текущий перечень полок:', polki())

'''5'''

def ds(number_polka: str) -> None:
 if number_polka not in directories.keys():
  print('Такой полки не существует.Текущий перечень полок: ', polki())
 elif not directories[number_polka]:
  directories.pop(number_polka)
  print('Полка удалена.Текущий перечень полок: ', polki())
 else:
  print('На полке есть документы, удалите их перед тем как удалять полку.Текущий перечень полок: ', polki())

'''6 '''

def ad(number_doc,type_doc , vl_doc, number_polki_xr):
    if int(number_polki_xr) == 1 or int(number_polki_xr) == 2 or int(number_polki_xr) == 3:
        documents.append({"number": number_doc,"type": type_doc,  "name": vl_doc})
        directories[number_polki_xr].append(number_doc)
        print('Документ добавлен. Текущий список документов:')
    else:
        print('Такой полки не существует. Добавьте полку командой as.\n Текущий список документов:')

'''7 '''
def d(number_doc):
    break_polka = False
    for doc in documents:
        if doc['number'] == number_doc:
            doc['number'] = 'Удален'
            for directory_value in directories.values():
                if number_doc in directory_value:
                    directory_value.remove(number_doc)
                    print('Документ удален.\n Текущий список документов: ')
                    break_polka = True
                    break
            if break_polka == True:
                break
    else:
        print('Документ не найден в базе. \n Текущий список документов: ')

'''8 '''

def m():
    znak = False
    if number_polki in directories:
        for inf in documents:
            if inf['number'] == number_doc:
                znak = True
                break
        if znak == True:
            for key in directories:
                for i in directories[key]:
                    if i == number_doc:
                        directories[key].remove(number_doc)
                        directories[number_polki].append(number_doc)
                        break
            print ("Документ перемещен.", "Текущий список документов:")
            l()
        else:
            print ("Документ не найден в базе.", "Текущий список документов:")
            l()
    else:
        print("Такой полки не существует. Текущий перечень полок:", polki())

while True:
    commanda = input('Введите команду(p, s, l, ads, ds, ad, d, m, d, m,q): ')
    if commanda == 'p':
        p(input('Введите номер документа:'))
    elif commanda == 's':
        s(input('Введите номер документа:'))
    elif commanda == 'l':
        l()
    elif commanda == 'ads':
        ads(input('Введите номер полки:'))
    elif commanda == 'ds':
        ds(input('Введите номер полки:'))
    elif commanda == 'ad':
        ad(input('Введите номер документа :'),
                    input('Введите тип документа: '), input('Введите владельца документа: '),
                        input('Введите полку для хранения: '))
        l()
    elif commanda == 'd':
        d(input('Введите номер документа:'))
        l()
    elif commanda == 'm':
        number_doc = input("Введите номер документа,который хоитите переместить: ")
        number_polki = input("Введит номер полки, на которую хоиите перемести документ: ")
        m()
    elif commanda == 'q':
        break
