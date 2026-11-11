import random


def gen_player_achievements(achievements) -> set:
    amount = random.randint(1, len(achievements))
    return set(random.sample(achievements, amount))


if __name__ == "__main__":
    print("=== Welcome to the Achievement Tracker! ===")

    achievements = [
        "First Blood",
        "Sharp Shooter",
        "Marathon Runner",
        "Master Collector",
        "Puzzle Master",
        "Speed Demon",
        "Stealth Assassin",
    ]

    all_achievements = set(achievements)

    vitor = gen_player_achievements(achievements)
    marcos = gen_player_achievements(achievements)
    igor = gen_player_achievements(achievements)

    print()

    print(f"Your random achievements are: {vitor}")
    print(f"Marcos's random achievements are: {marcos}")
    print(f"Igor's random achievements are: {igor}")

    print()

    all_unlocked = set.union(vitor, marcos, igor)
    print(f"All achievements: {all_unlocked}")

    print()

    shared = set.intersection(vitor, marcos, igor)
    print(f"Shared achievements: {shared}")

    print()

    vitor_unique = set.difference(vitor, marcos, igor)
    print(f"Vitor's unique achievements: {vitor_unique}")

    marcos_unique = set.difference(marcos, vitor, igor)
    print(f"Marcos's unique achievements: {marcos_unique}")

    igor_unique = set.difference(igor, vitor, marcos)
    print(f"Igor's unique achievements: {igor_unique}")

    print()

    vitor_missing = set.difference(all_achievements, vitor)
    print(f"Vitor's missing achievements: {vitor_missing}")

    marcos_missing = set.difference(all_achievements, marcos)
    print(f"Marcos's missing achievements: {marcos_missing}")

    igor_missing = set.difference(all_achievements, igor)
    print(f"Igor's missing achievements: {igor_missing}")
