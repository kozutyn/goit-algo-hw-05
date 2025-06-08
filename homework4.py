from typing import Callable

def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner

@input_error
def add_contact(args: list[str], contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: list[str], contacts: dict) -> str:
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def get_phone(args: list[str], contacts: dict) -> str:
    name = args[0]
    return f"{name}: {contacts[name]}"

@input_error
def get_all_contacts(args: list[str], contacts: dict) -> str:
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}

    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": get_phone,
        "all": get_all_contacts
    }

    while True:
        user_input = input("Enter a command: ").strip()

        if not user_input:
            print("Please enter a command.")
            continue

        if user_input.lower() in ("exit", "close", "good bye"):
            print("Good bye!")
            break

        parts = user_input.split()
        command = parts[0].lower()
        args = parts[1:]

        if command in commands:
            handler = commands[command]
            print(handler(args, contacts))
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
