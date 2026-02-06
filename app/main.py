import sys

inBuildCommands = ["echo", "exit", "type"]


def main():
    # TODO: Uncomment the code below to pass the first stage
    running = True
    while running:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit":
            running = False
        else: 
            handle_command(command)
    pass



def handle_command(command):
            
    match command.split()[0]:  
        case "echo":
            print(command.split(maxsplit=1)[1])
        case "type":
            if command.split(maxsplit=1)[1] in inBuildCommands:
                print(f"{command.split()[0]} is a shell built-in")
            else:
                print(f"{command.split()[0]} is not a shell built-in")
        case _:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()

