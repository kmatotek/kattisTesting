def max_k_collections():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    num_test_cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(num_test_cases):
        num_vases = int(data[index])
        index += 1
        shape_decoration_count = {}
        
        for __ in range(num_vases):
            s_i, d_i = int(data[index]), int(data[index + 1])
            index += 2
            if (s_i, d_i) not in shape_decoration_count:
                shape_decoration_count[(s_i, d_i)] = 0
            shape_decoration_count[(s_i, d_i)] += 1
        
        max_k = 0
        for count in shape_decoration_count.values():
            max_k = max(max_k, count)
        
        results.append(str(max_k))
    
    print("\n".join(results))