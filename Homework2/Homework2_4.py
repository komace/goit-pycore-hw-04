



# додаємо функцію яка приймає рядок вводу користувача і розбиває його на слова - метод split()
def parse_input(user_input):
    cmd, *args = user_input.split()
    # видаляємо зайві пробіли та перетворюємо на нижній регістр.
    cmd = cmd.strip().lower()     
    return cmd, *args

# додаємо функцію яка додає пару "ключ: значення" до словника контактів, 
# використовуючи ім'я як ключ і телефонний номер як значення
def add_contact(args, contacts):
    if len(args) != 2:
        return "Erorr: Invalid data. Provide: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return "Contact added"


# додаємо функцію яка замінює телефонний номер для контакту який вже був створений
def change_contact(args, contacts):
    if len(args) != 2:
        return "Erorr: Invalid data. Provide: add <name> <phone>"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact update"
    else:
        return "Error: Contact not found"



# додаємо функцію яка виводить телефонний номер за введеним контактом
def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: Invalid data. Provide: change <name> "
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Error: Contact not found."


# додаємо функцію яка виводить всі збережені контакти
def show_all(contacts):
    if not contacts:
        return "Contact not found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


# додаємо функцію яка входить в нескінчений цикл і очікує введення команди
def main():
    contacts = {}   # додаємо словник для контактів
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))   
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))               
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

    