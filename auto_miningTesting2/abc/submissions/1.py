def rearrange_numbers(numbers, order):
    sorted_numbers = sorted(numbers)
    mapping = {'A': sorted_numbers[0], 'B': sorted_numbers[1], 'C': sorted_numbers[2]}
    return [str(mapping[i]) for i in order]

def main():
    numbers = list(map(int, input().split()))
    order = input().strip()
    print(" ".join(rearrange_numbers(numbers, order)))

if __name__ == "__main__":
    main()