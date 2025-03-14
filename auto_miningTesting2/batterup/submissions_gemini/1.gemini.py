def calculate_slugging_percentage():
    """
    Calculates the slugging percentage based on user input.
    """

    number_of_at_bats = int(input())
    at_bat_outcomes = [int(x) for x in input().split()]

    valid_at_bats = 0
    total_bases = 0
    for outcome in at_bat_outcomes:
        if outcome != -1:  # Exclude walks
            valid_at_bats += 1
            total_bases += outcome

    slugging_percentage = total_bases / valid_at_bats
    print(slugging_percentage)

calculate_slugging_percentage()