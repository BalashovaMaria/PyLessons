import json

doc = "laba3.json"

def open_tasks():
    with open(doc, "r") as f:
        tasks = json.load(f)
    return tasks

def add(tasks):
    name = input('Сформулируйте задачу: ')
    category = input('Добавьте категорию к задаче: ')
    time = input('Добавьте время к задаче: ')
    tasks.append({'name': name, 'category': category, 'time': time})

def show(tasks):
    try:
        with open(doc, "w") as f:
            tasks = json.dump(tasks, f)
        print('Задачи сохранены в файл')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    tasks = open_tasks()
    print('Текущие задачи из файла: ', tasks)

    while True:
        print("""Простой todo: 
        1. Добавить задачу.
        2. Вывести список задач.
        3. Выход.""")
        command = int(input('Укажите число: '))
        if command == 1:
            add(tasks)
        elif command == 2:
            for task in tasks:
                print(f"Задача: {task['name']} Категория: {task['category']} Дата: {task['time']}")
        elif command == 3:
            show(tasks)
            break
        else:
            print('Введите команду из списка: ')
