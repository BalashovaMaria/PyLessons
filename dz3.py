#1
import random
nashe_chislo = random.randint(1,10)
while True:
    vashe_chislo=input("Ваше число: ")
    if int(vashe_chislo) == nashe_chislo:
        print("Это загаданное число")
        break
    elif int(vashe_chislo) > nashe_chislo:
        print("Ваше число больше загаданного")
    else:
        print("Ваше число меньше загаданного")
        
#2
import random
def new_pass():
    password = ""
    k = 0
    while k != 10:
        password += str(chr(random.randint(33,126)))
        k += 1
    return password
print(new_pass())

#3
passnew = input('vvedite parol:')
def nPass(password):
    if len(password) >= 8 and password.islower() == False and password.isupper() == False:
        for i in range(len(password)):
            if password[i].isdigit():
                return 'Принято!пароль отвечает требованиям надежности'
    return 'Ошибка!пароль не отвечает требованиям надежности ,введите новый'
print(nPass(passnew))




