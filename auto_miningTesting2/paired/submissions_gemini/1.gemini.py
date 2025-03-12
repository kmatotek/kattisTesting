def get_longest_two_appearance_subarray_length(array_length, numbers):
    """
    Finds the length of the longest consecutive sub-array where each element appears exactly twice.

    Args:
        array_length: The length of the input array.
        numbers: The input array of integers.

    Returns:
        The length of the longest valid sub-array.
    """

    max_length = 0
    for start_index in range(array_length):
        element_counts = {}
        current_length = 0
        for end_index in range(start_index, array_length):
            current_element = numbers[end_index]
            if current_element in element_counts:
                element_counts[current_element] += 1
            else:
                element_counts[current_element] = 1

            if element_counts[current_element] > 2:
                break

            current_length += 1
            if all(count == 2 for count in element_counts.values()):
                max_length = max(max_length, current_length)

    return max_length


if __name__ == "__main__":
    input_length = int(input())
    input_array = list(map(int, input().split()))
    result = get_longest_two_appearance_subarray_length(input_length, input_array)
    print(result)