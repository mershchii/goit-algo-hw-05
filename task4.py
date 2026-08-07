def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command."
        except IndexError:
            return "Enter user name."
        except KeyError:
            return 'Unregistered User.'

    return inner

@input_error
def add_contact(args, contacts: dict[str, str]):
    name, phone = args
    if phone in contacts:
        return "This phone is already available." # Додана перевірка на існування номера
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts: dict[str, str]):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts: dict[str, str]):
    name = args[0]  # Якщо args порожній -> IndexError
    return contacts[name]  # Якщо name немає -> KeyError

def show_all(contacts: dict[str, str]):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

@input_error
def parse_input(user_input: str):
    parts = user_input.strip().split()
    if not parts:
        raise ValueError("No command provided.")
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def main() -> None:
    contacts = {}

    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            print("No input provided. Please enter a command.")
            continue

        command, args = parse_input(user_input) # Виправлений баг

        if command == "add":
            result = add_contact(args, contacts)
            print(result)
        elif command == "change":
            result = change_contact(args, contacts)
            print(result)
        elif command == "phone":
            result = show_phone(args, contacts)
            print(result)
        elif command == "all":
            result = show_all(contacts)
            print(result)
        elif command == "exit":
            print("Goodbye!")
            break   

if __name__ == "__main__":
    main()
