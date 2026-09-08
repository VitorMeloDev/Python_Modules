import sys
from typing import IO

def save_file(content: str) -> None:
    print("Transform data:\n---")
    print(content)
    print("---")
    new_file = input("Enter new file name(or empty): ")
    if new_file:
        print(f"Saving data to '{new_file}'")
        file = open(new_file, "w")
        file.write(content)
        file.close()
        print(f"Data saved in file '{new_file}'.")
    else:
        print("Not saving data.")


def process_file(file_name: str) -> str:
    print(f"Accessing file '{file_name}'\n---")

    try:
        file = open(file_name)
        content = file.read()
        file.close()
        print (content)
        new_content = ""
        file = open(file_name)
        for line in file:
            new_content += line[:-1]+ "#\n"
        print("\n---")
        print(f"File '{file_name}' closed")
        file.close()
        return new_content
    except FileNotFoundError as error:
        print(error)
    except OSError as error:
        print(error)



if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) < 2:
        print("Error: Enter a name file")
    else:
        copy = process_file(sys.argv[1])
        save_file(copy)