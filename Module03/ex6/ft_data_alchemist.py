import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam"
    ]
    print(f"Initial list of players: {players}\n")

    capitalized = [player.capitalize() for player in players]
    print(f"New list with all names capitalized: {capitalized}")
    print()
    only_cap = [player for player in players if player[0].isupper()]
    print(f"New list of capitalized names only: {only_cap}")
    print()
    score = {player: random.randint(0, 1000) for player in players}
    print(f"Score dict: {score}")
    avg = sum(score.values()) / len(score)
    print(f"Average score is {avg:.2f}")
    print()
    high_scores = {player: score for player,
                   score in score.items() if score > avg}
    print(f"High score: {high_scores}")
