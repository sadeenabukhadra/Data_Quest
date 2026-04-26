import random


def gen_player_achievements() -> set[str]:
    achievements_list = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
        "Hidden Path Finder",
    ]

    num = random.randint(3, len(achievements_list))
    return set(random.sample(achievements_list, num))


def main() -> None:
    print("=== Achievement Tracker System ===")

    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for player in players:
        print(f"Player {player}: {players[player]}")

    all_achievements: set[str] = set()
    for ach in players.values():
        all_achievements = all_achievements.union(ach)

    print("\nAll distinct achievements:", all_achievements)

    common = None
    for ach in players.values():
        if common is None:
            common = ach
        else:
            common = common.intersection(ach)

    print("Common achievements:", common)

    for player, achievement in players.items():
        others: set[str] = set()

        for other_player, other_ach in players.items():
            if other_player != player:
                others = others.union(other_ach)

        unique = achievement.difference(others)
        print(f"Only {player} has: {unique}")

    for player, achievement in players.items():
        missing = all_achievements.difference(achievement)
        print(f"{player} is missing: {missing}")


if __name__ == "__main__":
    main()
