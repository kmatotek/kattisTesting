def find_max_k(vases):
    shapes = set()
    decorations = set()
    
    for shape, decoration in vases:
        shapes.add(shape)
        decorations.add(decoration)
    
    min_shape_count = len(shapes) // 2
    min_decoration_count = len(decorations) // 2
    
    k = min(min_shape_count, min_decoration_count)
    
    return k

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    results = []
    
    n = int(data[index])
    index += 1
    
    for _ in range(n):
        m = int(data[index])
        index += 1
        
        vases = []
        for _ in range(m):
            s_i = int(data[index])
            d_i = int(data[index + 1])
            index += 2
            vases.append((s_i, d_i))
        
        results.append(find_max_k(vases))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()