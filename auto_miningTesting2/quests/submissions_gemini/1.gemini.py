def calculate_max_xps(num_quests, xps_per_level, xp_multiplier, quests):
    """
    Calculates the maximum possible XPs earned by completing all quests
    in an optimal order.

    Args:
        num_quests (int): The number of quests.
        xps_per_level (int): XPs required to reach each level.
        xp_multiplier (int): XP multiplier for completing quests below target level.
        quests (list): List of tuples, each containing (xps, target_level) for a quest.

    Returns:
        int: The maximum possible XPs earned.
    """

    quests.sort(key=lambda q: q[1])  # Sort quests by target level ascending
    total_xps = 0
    current_level = 0
    earned_xps = 0

    for i in range(num_quests):
        xps, target_level = quests[i]

        if current_level >= target_level:
            earned_xps += xps
        else:
            earned_xps += xps * xp_multiplier

        total_xps = earned_xps
        current_level = earned_xps // xps_per_level  # Update current level

    return total_xps


def main():
    """
    Reads input, processes it, and prints the result.
    """

    num_quests, xps_per_level, xp_multiplier = map(int, input().split())
    quests = []
    for _ in range(num_quests):
        xps, target_level = map(int, input().split())
        quests.append((xps, target_level))

    max_xps = calculate_max_xps(
        num_quests, xps_per_level, xp_multiplier, quests
    )
    print(max_xps)


if __name__ == "__main__":
    main()