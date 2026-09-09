import sys
import typing


def save_file(content: str) -> None:
    print("Transform data:\n---")
    print(content)
    print("---")
    print("Enter new file name(or empty): ")

    new_file = sys.stdin.readline()
    new_file = new_file[:-1]

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

    content = ""

    try:
        file = open(file_name)
        content = file.read()
        file.close()

        print(content)

        new_content = ""
        file = open(file_name)

        for line in file:
            new_content += line[:-1] + "#\n"

        file.close()

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
        save_file(copy)