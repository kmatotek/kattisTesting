def calculate_count(num_of_digits):
  """
  Calculates the count of positive numbers with num_of_digits digits that don't contain a '9'.

  Args:
    num_of_digits: The number of digits.

  Returns:
    The count of positive numbers modulo 1,000,000,007.
  """
  total_count = 8  # Start with 8 for the first digit (1-8)
  current_count = 9  # 9 choices (0-8) for the remaining digits

  for _ in range(1, num_of_digits):
    total_count = (total_count * current_count) % 1000000007

  return total_count


def main():
  """
  Handles input and output for the program.
  """
  test_cases = int(input())
  for _ in range(test_cases):
    digits = int(input())
    result = calculate_count(digits)
    print(result)


if __name__ == "__main__":
  main()