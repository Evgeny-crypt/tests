documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '234 34222', '65433 23'],
    '3': []
}


def get_name_by_doc(document):
    name = ''
    doc_number = input("Введите номер документа: ")
    for document in documents:
        if doc_number == document['number']:
            name = document['name']
    if name != '':
        print(name)
    else:
        print("Ошибка: такого документа не существует!")


def get_data(document):
    for document in documents:
        print(document['type'], document['number'], document['name'])


def get_directory(directories):
    doc_number = input('Введите номер документа: ')
    shelf = ''
    for directory in directories:
        if doc_number in directories[directory]:
            shelf = directory
    if shelf != '':
        print(f'Документ находится на {shelf} полке')
    else:
        print('Ошибка! Такого документа нет')


def add_doc_by_params():
    doc_number = input('Введите номер документа: ')
    doc_type = input('Введите тип документа:')
    doc_owner = input('Введите имя владельца документа: ')
    doc_directory = input('Введите номер полки, на которой будет храниться документ: ')

    if doc_directory in directories:
        directories[doc_directory].append(doc_number)
        documents.append({"type": doc_type, "number": doc_number, "name": doc_owner})
        return documents, directories
    else:
        print("Ошибка! Такая полка отсутствует, документ не будет добавлен.")


def add_dir():
    shelf = input("Введите номер полки: ")
    if shelf not in directories:
        directories.update({shelf: []})
    else:
        print("Ошибка! такая полка уже есть.")


def move_document(directories):
    success = False
    doc_number = input("Введите номер документа: ")
    dir_requested = input("На какую полку переместить? ")
    for directory in directories:
        if doc_number in directories[directory] and dir_requested in directories:
            directories[directory].remove(doc_number)
            directories[dir_requested].append(doc_number)
            success = True
    if success == False:
        return 'Ошибка! документ или полка отсутствует.'
    else:
        return directories


def delete_document(documents, directories):
    success = False
    deleted_doc = input("Введите номер документа: ")
    for document in documents:
        if deleted_doc == document["number"]:
            documents.remove(document)
            success = True
    for directory in directories:
        if deleted_doc in directories[directory]:
            directories[directory].remove(deleted_doc)
            success = True
    if success != True:
        print("Ошибка! Такой документ не найден.")
    else:
        print("Документ удален.")
        return documents, directories



def commands():
    """
    p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит.
    l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
    d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
    m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
    as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;

    """
    command = input("Введите команду: ")
    if command == 'p':
        get_name_by_doc(documents)
    elif command == 'l':
        get_data(documents)
    elif command == 's':
        get_directory(directories)
    elif command == 'a':
        add_doc_by_params()
    elif command == 'd':
        delete_document(documents, directories)
    elif command == 'm':
        move_document(directories)
    elif command == 'as':
        add_dir()


if __name__ == '__main__':
    commands()
