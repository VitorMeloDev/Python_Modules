import random
from typing import Generator


def gen_event(
    players: list,
    actions: list
) -> Generator[tuple[str, str], None, None]:

    while True:
        yield (
            random.choice(players),
            random.choice(actions)
        )


def show_events(players: list, actions: list) -> None:
    act = gen_event(players, actions)

    for n in range(0, 1000):
        player, action = next(act)
        print(f"Event {n}: Player {player} did action {action}")


def create_list_of_events(players: list, actions: list) -> list:
    act = gen_event(players, actions)
    events = []

    for n in range(0, 10):
        event = next(act)
        events.append(event)

    return events


def consume_event(
    events: list
) -> Generator[tuple[str, str], None, None]:

    while events:
        event = random.choice(events)
        events.remove(event)
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    players = ["Vitor", "Marcus", "João"]
    actions = ["Fight", "Talk", "Run", "Pee",
               "Smoke", "Drink", "Sleep", "Eat", "Code"]

    show_events(players, actions)

    events = create_list_of_events(players, actions)

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")
