def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        2 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        "abc" + 123
    else:
        return


def test_error_types(test: int) -> None:
    try:
        garden_operations(test)
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    except TypeError as error:
        print(f"Caught TypeError: {error}")
    else:
        print("Operation completed successfully")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    for test in range(5):
        print(f"Testing operation {test}...")
        test_error_types(test)
    print()
    print("All error types tested successfully!")
