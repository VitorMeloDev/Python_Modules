import sys

if __name__ == "__main__":
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
    else:
        print("No arguments received.")
    print(f"Total arguments: {len(sys.argv)}")