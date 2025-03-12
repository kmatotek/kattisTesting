def slugging_percentage():
    num_at_bats = int(input())
    at_bats = list(map(int,input().split()))

    total_bases = 0
    official_at_bats = 0
    for bat in at_bats:
        if bat >= 0:
            total_bases += bat
            official_at_bats += 1

    slugging_percentage = total_bases / official_at_bats
    print("%.4f" % slugging_percentage)


slugging_percentage()