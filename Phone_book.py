import os

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phon.txt')

    while choice != 8:
        os.system('cls' if os.name == 'nt' else 'clear')  
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            result = find_by_lastname(phone_book, last_name)
            if result is not None:
                print_result([result])
            else:
                print("Абонент не найден")
        elif choice == 3:
            number = input('Введите номер: ')
            result = find_by_number(phone_book, number)
            if result is not None:
                print_result([result])
            else:
                print("Абонент не найден")
        elif choice == 4:
            last_name = input('Введите фамилию: ')
            print(delete_by_lastname(phone_book, last_name))
        elif choice == 5:
            user_data = input('Введите новые данные (Фамилия,Имя,Телефон,Описание): ')
            add_user(phone_book, user_data)
            write_txt('phon.txt', phone_book)
        elif choice == 6:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер: ')
            print(change_number(phone_book, last_name, new_number))
            write_txt('phon.txt', phone_book)
        elif choice == 7:
            print_result(phone_book)
            copy_record_to_file('phon.txt', 'new_phon.txt')
        elif choice == 8:
            print("Работа завершена")

        input("\nНажмите Enter для возврата в основное меню...")
        choice = show_menu()

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  
    print("\n Выберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Удалить абонента по фамилии\n"
          "5. Добавить абонента в справочник\n"
          "6. Изменить номер абонента\n"
          "7. Копировать строку из одного файла в другой\n"
          "8. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            if line.strip():  
                record = dict(zip(fields, line.strip().split(',')))
                phone_book.append(record)

    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            s = ','.join(record.values())
            phout.write(f'{s}\n')

def print_result(phone_book):
    max_lengths = {key: max(len(record[key]) for record in phone_book) for key in phone_book[0].keys()}

    for record in phone_book:
        print('\t'.join([f'{key}: {value.ljust(max_lengths[key] + 1)}' for key, value in record.items()]))

def find_by_lastname(phone_book, last_name):
    found_records = [record for record in phone_book if record['Фамилия'] == last_name]
    if found_records:
        return found_records[0]
    else:
        return None  

def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            return "Номер изменен"
    return "Абонент не найден"

def delete_by_lastname(phone_book, last_name):
    for i, record in enumerate(phone_book):
        if record['Фамилия'] == last_name:
            del phone_book[i]
            return "Абонент удален"
    return "Абонент не найден"

def find_by_number(phone_book, number):
    found_records = [record for record in phone_book if record['Телефон'] == number]
    if found_records:
        return found_records[0]
    else:
        return None  

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    phone_book.append(record)
    print("Новый абонент добавлен")

def copy_record_to_file(source_file, target_file):
    try:
        line_number = int(input("Введите номер строки для копирования: ")) - 1  
        with open(source_file, 'r', encoding='utf-8') as src, open(target_file, 'a', encoding='utf-8') as tgt:
            lines = src.readlines()
            if 0 <= line_number < len(lines):
                tgt.write(lines[line_number])
                print(f"Строка {line_number + 1} успешно скопирована из {source_file} в {target_file}")
            else:
                print(f"Ошибка: строка с номером {line_number + 1} не найдена в файле {source_file}")
    except ValueError:
        print("Ошибка: введите целое число для номера строки")
    except Exception as e:
        print(f"Произошла ошибка при копировании строки: {e}")


work_with_phonebook()





