def input_error(func):
    
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args.split()
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args.split()
    contacts[name] = phone
    return "Contact updated."

@input_error
def get_phone(args, contacts):
    name = args.strip()
    return contacts[name]

@input_error
def show_all(_, contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def parse_command(command_line):
    command_parts = command_line.strip().split(maxsplit=1)
    if not command_parts:
        return "", ""
    command = command_parts[0].lower()
    args = command_parts[1] if len(command_parts) > 1 else ""
    return command, args

def main():
    contacts = {}
    print("Welcome to assistant. Type 'exit', 'close' or 'good bye' to quit.")
    while True:
        user_input = input("Enter command: ").strip()
        if not user_input:
            print("Empty input. Please enter a command.")
            continue

        command, args = parse_command(user_input)

        if command in ("exit", "close", "good", "bye"):
            print("Good bye!")
            break
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Unknown command. Try: add, change, phone, all")

if __name__ == "__main__":
    main()
