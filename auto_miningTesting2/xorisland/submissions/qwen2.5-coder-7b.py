def find_xor_triple(hats):
    n = len(hats)
    for i in range(n):
        hat = hats[i]
        xor_count = [0] * 2**25
        for j in range(n):
            if i != j:
                xor_count[hat ^ hats[j]] += 1
        if xor_count[hat] > 0:
            return i + 1
    return -1

def find_days_to_hand_raising(hats):
    n = len(hats)
    meetings = [set() for _ in range(n)]
    
    # Initialize the XOR count for all islanders
    xor_counts = [[] for _ in range(n)]
    
    for i in range(n):
        hat = hats[i]
        for j in range(n):
            if i != j:
                xor_counts[i].append(hat ^ hats[j])
    
    # Find initial triples and mark the islanders involved
    initial_triples = []
    for i in range(n):
        if any(xor_val in xor_counts[i] for xor_val in xor_counts[i]):
            initial_triples.append(i)
    
    # Mark initial triples in meetings
    for i in initial_triples:
        meetings[i].add(i)

    day = 1
    while True:
        new_triples = []
        for i in range(n):
            if i not in meetings[i]:
                xor_count = [0] * (2**25)
                for j in meetings[i]:
                    xor_count[hats[j] ^ hats[i]] += 1
                if xor_count[hats[i]] > 0:
                    new_triples.append(i)
                    meetings[i].add(i)
        day += 1
        if not new_triples:
            break

    return day - 1

# Read input
n = int(input().strip())
hats = [int(input().strip()) for _ in range(n)]

# Find the number of days to hand raising
days = find_days_to_hand_raising(hats)

# Print output
print(days)