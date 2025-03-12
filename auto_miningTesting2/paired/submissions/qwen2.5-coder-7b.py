def max_subarray_length(array):
    index_map = {}  # To store the last seen indices of elements in the array
    start = result = 0  # Initialize start index to 0 and result to 0

    for i, num in enumerate(array):  
        if num in index_map:
            # If element is already present in dictionary, remove all indices before its previous occurrence 
            while start <= index_map[num]:
                del index_map[array[start]]    
                start += 1
                
        index_map[num] = i  # Update the last seen index of current number
        
    return result

# Read input
N = int(input())
array = [int(x) for x in input().split()]

# Call function and print output
print(max_subarray_length(array))