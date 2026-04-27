from typing import Generator
import random


def gen_event() -> tuple[str, str,None,None]:
    players = ["bob", "alice", "dylan", "charlie"]
    actions = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "release"]
    while True:
        random_players = random.choice(players)
        random_actions = random.choice(actions)
        yield (random_players, random_actions)
def consume_event(events:list[tuple[str,str]]):
        while events:
            index = random.randint(0,len(events)-1)
            event = events.pop(index)
            yield event

def main() -> None:
    print("=== Game Data Stream Processor ===")

    g = gen_event()
    for i in range(1000):
        event = next(g)
        print(
            f"Event {i}:Player {event[0]} "
            f"did action{event[1]}")
    events_list=[next(g) for _ in range(10)]
    print(f"Built list of 10 events: {events_list}")

    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")
if __name__ == "__main__":
    main()
