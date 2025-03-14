from math import factorial

def calculate_probability(remaining_votes, votes_needed):
    """Calculates the probability of winning given the remaining votes and votes needed."""
    total_combinations = 2**remaining_votes
    favorable_combinations = 0
    for wins in range(votes_needed, remaining_votes + 1):
        favorable_combinations += factorial(remaining_votes) // (factorial(wins) * factorial(remaining_votes - wins))
    return (favorable_combinations / total_combinations) * 100

def analyze_election(total_votes, candidate1_votes, candidate2_votes, win_threshold):
    """Analyzes the election results and provides a recommendation."""
    remaining_votes = total_votes - candidate1_votes - candidate2_votes
    votes_needed = (total_votes // 2) + 1 - candidate1_votes

    if votes_needed <= 0:
        return "GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!"
    elif votes_needed > remaining_votes:
        return "RECOUNT!"
    else:
        probability_of_winning = calculate_probability(remaining_votes, votes_needed)
        if probability_of_winning > win_threshold:
            return "GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!"
        else:
            return "PATIENCE, EVERYONE!"

# Read the number of test cases
test_cases = int(input())

# Process each test case
for _ in range(test_cases):
    # Read the election data
    total_votes, candidate1_votes, candidate2_votes, win_threshold = map(int, input().split())

    # Analyze the election and print the recommendation
    print(analyze_election(total_votes, candidate1_votes, candidate2_votes, win_threshold))