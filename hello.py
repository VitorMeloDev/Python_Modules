def main():
    name = input("Enter your name: ")
    greet_user(name)

def greet_user(to="world") -> None:
    print(f"Hello, {to}!")

main()