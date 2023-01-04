
def decor(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return "Sorry, try again"
    return wrapper



def hello():
    return "How can I help you?"


CBOOK = {}

@decor
def add(*args):
    name = args[0]
    phone = args[1]
    CBOOK[name] = phone
   
    return "Contact added"
 
@decor
def change(*args):
    name = args[0]
    phone = args[1]
    CBOOK[name] = phone

    return f"Contact {name} changed"

@decor
def phone(*args):
    name = args[0]
    
    return f"Contact {name} {CBOOK[name]}"


@decor
def show_all(*args):
    return CBOOK


@decor
def exit():
    return "Good bye!"
    


COMMANDS = {    
    hello: "hello",
    add: "add",
    change: "change",
    phone: "phone",
    show_all: "show",
    exit: ("good bye", "close", "exit")

}


def command_parser(user_input: str):
    for command, key_word in COMMANDS.items():
        if user_input.startswith(key_word):
            return command, user_input.replace(key_word, "").strip().split()
    return None, None




def main():
    contact_book = {}

    while True:
        user_input = input(">>>")
        if user_input == "good bye" or user_input == "close" or user_input == "exit":
            print(exit())
            break
        command, data = command_parser(user_input)
        
        if not command:
            print("Sorry, unknown command")
        else:
            print(command(*data))


if __name__ == "__main__":
    main()




