def rearrange_numbers(A, B, C, desired_order):
    # Create a dictionary to map each letter to its corresponding number
    number_map = {'A': A, 'B': B, 'C': C}
    
    # Sort the numbers based on their order in the desired order string
    sorted_numbers = [number_map[letter] for letter in desired_order]
    
    # Print the sorted numbers separated by a space
    print(" ".join(map(str, sorted_numbers)))

# Read input from user
A, B, C = map(int, input().split())
desired_order = input().strip()

# Call the function to rearrange and print the numbers
rearrange_numbers(A, B, C, desired_order)