import random


def gen_player_achievement(achievements):
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

    vitor = gen_player_achievement(achievements)
    marcos = gen_player_achievement(achievements)
    igor = gen_player_achievement(achievements)

    print()

    print(f"Your random achievements are: {vitor}")
    print(f"Marcos's random achievements are: {marcos}")
    print(f"Igor's random achievements are: {igor}")

    print()

    all_unlocked = vitor | marcos | igor
    print(f"All achievements: {all_unlocked}")

    print()

    shared = vitor & marcos & igor
    print(f"Shared achievements: {shared}")

    print()

    vitor_unique = vitor - (marcos | igor)
    print(f"Vitor's unique achievements: {vitor_unique}")

    marcos_unique = marcos - (vitor | igor)
    print(f"Marcos's unique achievements: {marcos_unique}")

    igor_unique = igor - (vitor | marcos)
    print(f"Igor's unique achievements: {igor_unique}")

    print()

    vitor_missing = all_achievements - vitor
    print(f"Vitor's missing achievements: {vitor_missing}")

    marcos_missing = all_achievements - marcos
    print(f"Marcos's missing achievements: {marcos_missing}")

    igor_missing = all_achievements - igor
    print(f"Igor's missing achievements: {igor_missing}")
