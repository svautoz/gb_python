# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных
file_name = "phonebook.txt"

def print_file():
    with open(file_name, "r", encoding="utf-8") as file:
        print(file.read())

def delete_record(rec_num):
    with open(file_name, "r", encoding="utf-8") as file:
        rec_list = file.readlines()
    if rec_num >= len(rec_list) or rec_num <= 0:
        return   
    del rec_list[rec_num - 1]
    with open(file_name, "w", encoding="utf-8") as file:
        file.writelines(rec_list)

def mod_record(rec_num):
    with open(file_name, "r", encoding="utf-8") as file:
        rec_list = file.readlines()
    if rec_num >= len(rec_list) or rec_num <= 0:
        return   
    new_rec = input(f"Введите новые данные для строки {rec_num}:")
    rec_list[rec_num - 1] = new_rec + "\n"
    with open(file_name, "w", encoding="utf-8") as file:
        file.writelines(rec_list)


print("Команды:\n1.Вывести данные - print\n2.Удалить данные - del \'номер строки\'\n3.Изменить данные - mod \'номер строки\'\n4.Выйти - exit")
while True:
    command = input("Введите команду:").split()
    match command[0]:
        case "print": 
            print_file()
        case "del": 
            if len(command) > 1 and command[1].isdigit():
                delete_record(int(command[1])) 
        case "mod": 
            if len(command) > 1 and command[1].isdigit():
                mod_record(int(command[1]))   
        case "exit":
            break     
        case _:
            break    