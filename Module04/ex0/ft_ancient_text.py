import sys
from typing import IO

def process_file(file_name: str) -> None:
    print(f"Accessing file '{file_name}'\n---")

    try:
        file = open(file_name)
        content = file.read()
        print (content)
        file.close()
    except FileNotFoundError as error:
        print(error)
    except OSError as error:
        print(error)
    print("\n---")
    print(f"File '{file_name}' closed")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) < 2:
        print("Error: Enter a name file")
    else:
        process_file(sys.argv[1])