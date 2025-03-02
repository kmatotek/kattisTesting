mport sys

def find_accepted_groups(seats, groups):
    accepted_groups = []
    for group in groups:
        if seats >= group:
            accepted_groups.append(group)
            seats -= group
        else:
            break
    return len(groups) - len(accepted_groups)

if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n_seats, n_groups = data[0], data[1]
    groups = list(map(int, input.split()))[2:]
    print(find_accepted_groups(n_seats, groups)