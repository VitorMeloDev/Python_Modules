import sys


def process_file(file_name: str) -> None:
    print(f"Accessing file '{file_name}'")

    try:
        file = open(file_name, "r")
        content = file.read()
        print("---")
        print(content.strip())
        print("---")
        file.close()
        print(f"File '{file_name}' closed.")
    except (FileNotFoundError, PermissionError, OSError) as error:
        print(f"Error opening file '{file_name}': {error}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <filename>")
    else:
        print("=== Cyber Archives Recovery ===")
        process_file(sys.argv[1])
