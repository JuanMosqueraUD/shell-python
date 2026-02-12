import sys
import os
import subprocess

inBuildCommands = ["echo", "exit", "type", "pwd", "cd"]
path = os.environ["PATH"].split(os.pathsep)

def main():
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
    parts = command.split()
    commandPrefix = parts[0]
    #" ".join une las partes separadas por espacios
    commandComplement = " ".join(parts[1:])
    #switch case altas comparaciones de comandos
    match commandPrefix:  
        case "echo":
            print(commandComplement)
        case "type":
            if commandComplement in inBuildCommands:
                print(f"{commandComplement} is a shell builtin")
            else:
                imported= pathComands(commandComplement)
                if imported:
                    print(f"{commandComplement} is {imported}")
                else:
                    print(f"{commandComplement}: not found")
        case "pwd":
            current_dir = os.getcwd()
            print(current_dir)
        case "cd":
            change_directory(commandComplement)
        case _:
            pathCommand = pathComands(commandPrefix)
            if pathCommand:
                #subprocess.run es el estandar actual para correr programas externos
                subprocess.run([commandPrefix] + parts[1:])
            else:
                print(f"{command}: command not found")

def pathComands(command):
 
    for dir in path:
        fullPath = os.path.join(dir, command)
        # verifica que el archivo existe os.isfile y es ejecutable os.x_ok
        if os.path.isfile(fullPath) and os.access(fullPath, os.X_OK):
            return fullPath
    return None

def change_directory(path):
    home_dir = os.path.expanduser("~")
    if path == "~":
        os.chdir(home_dir)
    else:
        try:
            os.chdir(path)
        except FileNotFoundError:
            print(f"cd: {path}: No such file or directory")

if __name__ == "__main__":
    main()

