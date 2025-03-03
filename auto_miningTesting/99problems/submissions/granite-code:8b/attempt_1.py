def round_up_to_99(price):
    return round(price / 100) * 100 + 99
input_price = int(input())
output_price = round_up_to_99(input_price)
print(output_price)