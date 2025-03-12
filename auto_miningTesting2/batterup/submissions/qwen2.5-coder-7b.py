def calculate_slugging_percentage(at_bats):
    total_bases = 0
    official_at_bats_count = 0
    
    for at_bat in at_bats:
        if at_bat == -1: 
            continue  # skip walks (represented by -1)
        total_bases += at_bat
        official_at_bats_count += 1
    
    slugging_percentage = total_bases / official_at_bats_count
    return slugging_percentage

# read input
n = int(input().strip())
at_bats = list(map(int, input().strip().split()))

# calculate and print the slugging percentage
slugging_percentage = calculate_slugging_percentage(at_bats)
print(slugging_percentage)