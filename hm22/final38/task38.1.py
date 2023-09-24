def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Добавить абонента в справочник\n"
          "4. Удалить абонента из справочника\n")
    choice = int(input())
    return choice


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')

    while (choice != 5):
        if choice == 1:  # 1. Отобразить весь справочник
            print(phone_book)
        elif choice == 2:  # 2. Найти абонента по фамилии
            name = get_search_name()
            print(find_by_name(phone_book, name))
        elif choice == 3:  # 3. Добавить абонента в справочник
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv('phonebook.csv', phone_book)
        elif choice == 4:  # 4. Удалить абонента из справочника
            name = get_search_name()
            print(find_by_name(phone_book, name))
            delete_user(phone_book, find_by_name(phone_book, name))
            write_csv('phonebook.csv', phone_book)
        choice = show_menu()

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def find_by_name(data: list, first_name):
    search_by_name = []
    for line in data:
        index = line['Фамилия'].lower()
        if index.find(first_name.lower()) == 0:
            search_by_name.append(dict(line))
    return search_by_name

def get_new_user():
    line = {}
    fields = ["Фамилия", "Имя", "Телефон"]
    for v in fields:
        data = input(f'Введите {v}: ')
        line[v] = data
    return line


def delete_user(data: list, name):
    tmp = []
    for record in name:
        if record in data:
            print('Найдена запись для удаления:')
            tmp.append(record)
            print(tmp)
            confirmation = input('Для подтверждения удаления записи введите ""yes"",\n'
                                 'для отмены операции удаления введите ""no"":')
            if confirmation == 'yes':
                data.remove(record)
            elif confirmation == 'no':
                return
            tmp.clear()

def add_user(data: list, user_data: dict):
    data.append(dict(user_data))
    return data

def get_search_name():
    first_name = input("Введите фамилию: ")
    return first_name

work_with_phonebook()