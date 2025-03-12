def zoo_inventory():
    test_case = 1
    while True:
        n = int(input())
        if n == 0:
            break
        
        animals = {}
        
        for _ in range(n):
            animal_name = input()
            # Splitting the animal name and taking the last part as the type of animal
            parts = animal_name.split()
            animal_type = parts[-1].lower()
            
            # Counting the occurrences of each type of animal
            if animal_type in animals:
                animals[animal_type] += 1
            else:
                animals[animal_type] = 1
        
        print(f"List {test_case}:")
        for animal, count in sorted(animals.items()):
            print(f"{animal} | {count}")
        
        test_case += 1

if __name__ == "__main__":
    zoo_inventory()