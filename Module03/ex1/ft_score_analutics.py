import sys

def process(numbers) -> None:
    print(f"Total players: {len(numbers)}")
    print(f"Total score: {sum(numbers)}")
    print(f"Average score: {sum(numbers) / len(numbers)}")
    print(f"High score: {max(numbers)}")
    print(f"Low Score: {min(numbers)}")
    print(f"Score range: {max(numbers) - min(numbers)}")

    
def message() -> str:
    return "No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ... <scoreN>"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(message())
    else:
        numbers = []
        for arg in sys.argv[1:]:
            try:
                score = int(arg)
                numbers.append(score)
            except ValueError:
                print(f"Invalid parameter: '{arg}'")
        if not numbers:
            print(message())
        else:
            process(numbers)