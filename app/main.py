import sys
import os

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
    #" ".join une las partes separadas por espacios
    commandComplement = " ".join(command.split()[1:])
    #switch case altas comparaciones de comandos
    match commandPrefix:  
        case "echo":
            print(commandComplement)
        case "type":
            if commandComplement in inBuildCommands:
                print(f"{commandComplement} is a shell builtin")
            else:
                imported= importedComands(commandComplement)
                if imported:
                    print(f"{commandComplement} is {imported}")
                else:
                    print(f"{commandComplement}: not found")
        case _:
            print(f"{command}: command not found")

def importedComands(command):
    path = os.environ["PATH"].split(os.pathsep)
    for dir in path:
        fullPath = os.path.join(dir, command)
        if os.path.isfile(fullPath) and os.access(fullPath, os.X_OK):
            return fullPath
    return None



if __name__ == "__main__":
    main()

