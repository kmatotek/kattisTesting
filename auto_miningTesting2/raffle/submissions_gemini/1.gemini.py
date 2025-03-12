from fractions import Fraction

def calculate_win_probability(total_names_excluding_yours, num_prizes):
  """Calculates the maximum probability of winning a prize in a raffle.

  Args:
    total_names_excluding_yours: The number of names in the raffle box excluding yours.
    num_prizes: The number of prizes to be given away.

  Returns:
    The maximum probability of winning a prize as a float.
  """

  max_probability = 0
  for num_entries in range(1, num_prizes + 1):
    probability_numerator = 0
    for prizes_won in range(1, num_entries + 1):
      # Calculate the probability of winning exactly 'prizes_won' prizes
      probability_numerator += (
          Fraction(total_names_excluding_yours, total_names_excluding_yours + num_entries - prizes_won) *
          Fraction(num_entries - prizes_won + 1, num_prizes - prizes_won + 1)
      )

    probability = float(probability_numerator)
    max_probability = max(max_probability, probability)

  return max_probability


if __name__ == "__main__":
  input_line = input().split()
  total_names_excluding_yours = int(input_line[0])
  num_prizes = int(input_line[1])

  max_win_probability = calculate_win_probability(total_names_excluding_yours, num_prizes)
  print(f"{max_win_probability:.6f}")