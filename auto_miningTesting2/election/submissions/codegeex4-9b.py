from math import comb

def shouldCelebrate(N, V1, V2, W):
    total_votes = N
    votes_for_candidate_1 = V1
    votes_for_candidate_2 = V2
    win_probability_threshold = W / 100

    # Calculate the number of remaining votes
    remaining_votes = total_votes - (votes_for_candidate_1 + votes_for_candidate_2)

    # Initialize the probability of winning to zero
    probability_winning = 0.0

    # Iterate over all possible outcomes for the remaining votes
    for i in range(remaining_votes + 1):
        # Calculate the number of votes for candidate 1 if i votes go to candidate 1
        votes_if_i_go_to_candidate_1 = votes_for_candidate_1 + i
        # Calculate the number of votes for candidate 2 if i votes go to candidate 2
        votes_if_i_go_to_candidate_2 = votes_for_candidate_2 + (remaining_votes - i)

        # If candidate 1 has more votes than half plus one, calculate the probability
        if votes_if_i_go_to_candidate_1 > total_votes / 2:
            probability_winning += comb(remaining_votes, i) * (0.5 ** remaining_votes)

    # Check if the calculated probability is greater than the threshold
    if probability_winning > win_probability_threshold:
        return "GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!"
    else:
        return "PATIENCE, EVERYONE!"

# Read the number of test cases
T = int(input().strip())

# Process each test case
results = []
for _ in range(T):
    N, V1, V2, W = map(int, input().strip().split())
    result = shouldCelebrate(N, V1, V2, W)
    results.append(result)

# Output the results for each test case
for result in results:
    print(result)