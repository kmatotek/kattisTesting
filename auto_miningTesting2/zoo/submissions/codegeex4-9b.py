def zoo_inventory():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    index = 0
    list_number = 1
    
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
        
        print(f"List {list_number}:")
        sorted_animals = sorted(animals.items())
        for animal, count in sorted_animals:
            print(f"{animal} | {count}")
        list_number += 1