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
    commandPrefix = command.split()[0]
    commandComplement = " ".join(command.split()[1:])
    match commandPrefix:  
        case "echo":
            print(commandComplement)
        case "type":
            if commandComplement in inBuildCommands:
                print(f"{commandComplement} is a shell builtin")
            else:
                print(f"{commandComplement}: not found")
        case _:
            print(f"{command}: command not found")
        


if __name__ == "__main__":
    main()

