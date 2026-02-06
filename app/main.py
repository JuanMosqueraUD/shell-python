import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    running = True
    while running:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit":
            running = False
        print(f"{command}: command not found")
    pass


if __name__ == "__main__":
    main()
