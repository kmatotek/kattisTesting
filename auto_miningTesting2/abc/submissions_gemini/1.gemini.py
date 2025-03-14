def rearrange_integers(num1, num2, num3, order):
  """Rearranges three integers in a specified order.

  Args:
    num1: The first integer.
    num2: The second integer.
    num3: The third integer.
    order: A string specifying the desired order, e.g., "ABC", "CAB".

  Returns:
    A string with the rearranged integers separated by spaces.
  """
  if not (num1 < num2 < num3):
    # Sort the numbers in ascending order if not already sorted
    num1, num2, num3 = sorted([num1, num2, num3])

  # Create a dictionary to map order characters to corresponding numbers
  order_map = {'A': num1, 'B': num2, 'C': num3}

  # Rearrange the numbers based on the specified order
  result = []
  for char in order:
    result.append(str(order_map[char]))

  return " ".join(result)

# Get input values
num1, num2, num3 = map(int, input().split())
desired_order = input()

# Rearrange and print the numbers
rearranged_numbers = rearrange_integers(num1, num2, num3, desired_order)
print(rearranged_numbers)