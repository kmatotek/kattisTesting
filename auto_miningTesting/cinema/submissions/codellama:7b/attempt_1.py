N = int(input())
M = int(input())
seats = []
for i in range(M):
    seats.append(int(input()))
accepted_groups = 0
rejected_groups = 0
for group in seats:
    if accepted_groups + group <= N:
        accepted_groups += group
    else:
        rejected_groups += 1
print(rejected_groups)