import sys


def save_file(content: str) -> None:
    print("Transform data:\n---")
    print(content)
    print("---")
    print("Enter new file name(or empty): ")

    new_file = sys.stdin.readline()
    new_file = new_file.rstrip("\r\n")

    if new_file:
        print(f"Saving data to '{new_file}'")

        try:
            file = open(new_file, "w")
            file.write(content)
            file.close()
            print(f"Data saved in file '{new_file}'.")
        except OSError as error:
            sys.stderr.write(
                f"[STDERR] Error opening file '{new_file}': {error}\n"
            )
            print("Data not saved.")
    else:
        print("Not saving data.")


def process_file(file_name: str) -> str:
    print(f"Accessing file '{file_name}'\n---")

    try:
        file = open(file_name)
        content = file.read()
        file.close()

        print(content)
        lines = content.splitlines()
        new_content = "\n".join(f"{line}#" for line in lines)
        if content.endswith(("\n", "\r")):
            new_content += "\n"

        print("\n---")
        print(f"File '{file_name}' closed")

        return new_content
    except OSError as error:
        sys.stderr.write(
            f"[STDERR] Error opening file '{file_name}': {error}\n"
        )
        return ""


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")

    if len(sys.argv) < 2:
        sys.stderr.write("[STDERR] Error: Enter a name file\n")
    else:
        copy = process_file(sys.argv[1])

        if len(copy) > 0:
            save_file(copy)
