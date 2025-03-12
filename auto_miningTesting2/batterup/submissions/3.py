def calculate_slugging_percentage():
    # Read the number of at-bats
    num_at_bats = int(input())

    # Read each result of at-bats
    at_bats = list(map(int, input().split()))

    # Initialize total number of bases and total number of non-walk at-bats
    total_bases = 0
    non_walk_at_bats = 0

    # Calculate total bases and number of non-walk at-bats
    for at_bat in at_bats:
        if at_bat != -1:
            total_bases += at_bat
            non_walk_at_bats += 1

    # Calculate and print the slugging percentage
    if non_walk_at_bats != 0:
        slugging_percentage = total_bases / non_walk_at_bats
        print(slugging_percentage)
    else:
        print("No official at-bats")

# Test the function
calculate_slugging_percentage()