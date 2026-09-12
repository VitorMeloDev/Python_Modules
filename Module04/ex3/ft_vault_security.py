def secure_archive(file_name: str, operation: str = "read", content: str = "") -> tuple[bool, str]:
    if operation == "read":
        try:
            with open(file_name, "r") as file:
                content = file.read()
            return True, content
        except OSError as error:
            return False, str(error)
    elif operation == "write":
        try:
            with open(file_name, "w") as file:
                file.write(content)
            return True, "Content successfully written to file"
        except OSError as error:
            return False, str(error)
    return False, "Invalid operation"


def main() -> None:
    print("=== Cyber Archives Security ===")

    # ==========================================================
    # Test 1: arquivo que não existe
    # ==========================================================

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    result = secure_archive("/not/existing/file", "read")
    print(result)

    # ==========================================================
    # Test 2: arquivo protegido
    # ==========================================================

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    result = secure_archive("/etc/shadow", "read")
    print(result)

    # ==========================================================
    # Test 3: arquivo que existe
    # ==========================================================

    print("\nUsing 'secure_archive' to read from a regular file:")
    result = secure_archive("/etc/hostname", "read")
    print(result)

    # ==========================================================
    # Test 4: criar um novo arquivo
    # ==========================================================

    print("\nUsing 'secure_archive' to write previous content to a new file:")

    content = result[1]

    result = secure_archive(
        "archive_test.txt",
        "write",
        content
    )

    print(result)

    # ==========================================================
    # Test 5: ler o arquivo que acabamos de criar
    # ==========================================================

    print("\nReading the newly created archive:")
    result = secure_archive("archive_test.txt", "read")
    print(result)


if __name__ == "__main__":
    main()