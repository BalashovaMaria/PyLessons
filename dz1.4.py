firstname=input('your firstname:')
if len(firstname)<5:
    surname=input('your surname:')
    name=firstname + surname
    print(name.upper())
else:
    print(firstname.lower())