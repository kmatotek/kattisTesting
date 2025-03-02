#input
N=int(input())
#define variables
closest_number=None
diff=float('inf')
#create a list of numbers ending in 99
numbers=[i for i in range(N,N+10000) if str(i)[-2:]=='99']
#loop through the list and find the closest number to N that ends in 99
for i in numbers:
    #calculate the difference between N and the current number
    curr_diff=abs(N-i)
    #if the difference is smaller than the previous smallest difference, set it as the closest number
    if curr_diff<diff:
        closest_number=i
        diff=curr_diff
#print the closest number to N that ends in 99
print(closest_number)