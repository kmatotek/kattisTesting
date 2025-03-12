def count_animals():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    index = 0
    results = []
    
    while index < len(data):
        n = int(data[index])
        if n == 0:
            break
        index += 1
        animals = {}
        
        for _ in range(n):
            animal = data[index].lower().split()[-1]
            if animal in animals:
                animals[animal] += 1
            else:
                animals[animal] = 1
            index += 1
        
        sorted_animals = sorted(animals.items())
        result = f"List {len(results) + 1}:"
        for animal, count in sorted_animals:
            result += f"\n{animal} | {count}"
        results.append(result)
    
    for result in results:
        print(result)