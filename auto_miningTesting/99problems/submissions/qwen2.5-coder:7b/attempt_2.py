# Read the input price from standard input
price = int(input())

# Calculate the lower multiple of 100 that is less than or equal to the given price
lower_multiple = (price // 100) * 100

# Calculate the upper multiple of 100 that is greater than the given price
upper_multiple = lower_multiple + 100

# Determine which multiple is closer to the given price
if price - lower_multiple <= upper_multiple - price:
    closest_price = lower_multiple if price - lower_multiple < upper_multiple - price else upper_multiple
else:
    closest_price = upper_multiple

# Print the closest price ending in 99
print(closest_price)