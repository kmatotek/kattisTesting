def rearrange_numbers():
    # Read input
    A, B, C = map(int, input().split())
    order = list(input())

    # Rearrange numbers according to order
    if order[0] == 'A':
        A, B, C = min(A, B, C), A, max(A, B, C)
    elif order[1] == 'B':
        B, C, A = min(B, C, A), B, max(B, C, A)
    else:
        C, A, B = min(C, A, B), C, max(C, A, B)

    # Print output
    print(A, B, C)


if __name__ == "__main__":
    rearrange_numbers()