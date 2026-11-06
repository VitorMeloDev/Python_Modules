import sys


def process_file(file_name: str) -> str:
    print(f"Accessing file '{file_name}'")

    try:
        content = open(file_name, "r").read()
        print("---")
        print(content.strip())
        print("---")
        print(f"File '{file_name}' closed.")

        lines = content.splitlines()
        transformed_content = "\n".join(f"{line}#" for line in lines)
        if lines:
            transformed_content += "\n"

        return transformed_content

    except (FileNotFoundError, PermissionError, OSError) as error:
        print(f"Error opening file '{file_name}': {error}")
        return ""


def save_file(content: str) -> None:
    print("\nTransform data:")
    print("---")
    print(content.strip())
    print("---")

    new_file = input("Enter new file name (or empty): ").strip()

    if new_file:
        print(f"Saving data to '{new_file}'")
        try:
            with open(new_file, "w") as file:
                file.write(content)
            print(f"Data saved in file '{new_file}'.")
        except (PermissionError, OSError) as error:
            print(f"Error saving file '{new_file}': {error}")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ft_archive_creation.py <filename>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        transformed_data = process_file(sys.argv[1])

        if transformed_data:
            save_file(transformed_data)
