def find_nearest_price(N):
    """
    Finds the nearest positive integer to N which ends in 99.

    Args:
        N: The price of a product.

    Returns:
        The nearest positive integer to N which ends in 99.
    """

    # Find the nearest integer to N which ends in 99.
    nearest_price = (N // 99) * 99

    # Check if the nearest integer is greater than or equal to N.
    if nearest_price >= N:
        return nearest_price
    else:
        return nearest_price + 99


# Read the input.
N = int(input())

# Find the nearest price.
nearest_price = find_nearest_price(N)

# Print the nearest price.
print(nearest_price)