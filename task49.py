def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
            "1. Отобразить весь справочник\n"
            "2. Найти абонента по фамилии\n"
            "3. Найти абонента по номеру телефона\n"
            "4. Добавить абонента в справочник\n"
            "5. Закончить работу")
    choice = int(input())
    return choice


def work_with_phonebook():
    choice = show_menu()

    phone_book = read_csv('phonebook.csv')

    while (choice != 5):

        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('lastname ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            number = input('number ')
            print(find_by_lastname(phone_book, number))
        elif choice == 4:
            last_name = input('lastname ')
            first_name = input('firstname ')
            number = input('number ')
            specification = input('specification ')
            print(new_subscriber(last_name, first_name, number, specification))


        choice = show_menu()


def read_csv(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields,   line.split(',')))
            phone_book.append(record)

    return phone_book


def new_subscriber(lastname, firstname, number, specification):
    with open('phonebook.csv', 'a', encoding='utf-8') as phout:
        new_sub = [lastname, firstname, number, specification]
        s = ''
        for i in new_sub:
            s+= i+','
        phout.write(f'{s[:-1]}\n')
        # phout.write(result)

        # for i in range(len(phone_book)):
        #     s = ''
        #     for v in phone_book[i].values():
        #         s+= v+','
        #     phout.write(f'{s[:-1]}\n')


def print_result(filename):
    for i in filename:
        print(i)


def find_by_lastname(phone_book, filename):
    for i in phone_book:
        for j in i.values():
            if filename == j:
                return i.values()

work_with_phonebook()