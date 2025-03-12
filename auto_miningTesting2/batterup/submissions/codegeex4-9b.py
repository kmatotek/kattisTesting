def calculate_slugging_percentage():
    # Read the number of at-bats from input
    n = int(input().strip())
    
    # Read the at-bat outcomes and convert them to a list of integers
    at_bats = list(map(int, input().strip().split()))
    
    # Initialize total bases and total official at-bats
    total_bases = 0
    total_official_at_bats = 0
    
    # Iterate through each at-bat outcome
    for at_bat in at_bats:
        # If the at-bat is not a walk, add its value to total bases and increment total official at-bats
        if at_bat != -1:
            total_bases += at_bat
            total_official_at_bats += 1
    
    # Calculate slugging percentage as total bases divided by total official at-bats
    slugging_percentage = total_bases / total_official_at_bats
    
    # Print the slugging percentage without rounding
    print(slugging_percentage)

# Call the function to execute
calculate_slugging_percentage()