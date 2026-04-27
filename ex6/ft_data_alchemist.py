import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()
    initial_list = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    print(f"Initial list of players: {initial_list}")
    capitalized_list: list[str] = [name.capitalize() for name in initial_list]
    print(f"New list with all names capitalized:{capitalized_list}")
    capitalized_list_only: list[str] = [
        name for name in capitalized_list if name[0].isupper()
    ]
    print(f"New list of capitalized names only: {capitalized_list_only}")
    scores: dict[str, int] = {}
    for name in capitalized_list:
        scores[name] = random.randint(50, 1000)
    print(f"Score dict: {scores}")
    avg: float = sum(scores.values()) / len(scores)
    print(f"Score average is {round(avg, 2)} ")
    high_score: dict[str, int] = {
        name: score for name, score in scores.items() if score > avg
    }
    print(f"High scores:{high_score}")


if __name__ == "__main__":
    main()
