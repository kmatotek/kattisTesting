def count_animals(test_input):
    from collections import defaultdict
    
    test_number = 1
    test_index = 0
    while test_index < len(test_input):
        n = test_input[test_index]
        test_index += 1
        if n == 0:
            break

        animal_counts = defaultdict(int)
        
        for _ in range(n):
            animal = test_input[test_index].strip().lower()
            test_index += 1
            animal_name = animal.split()[-1]
            animal_counts[animal_name] += 1

        sorted_animal_counts = sorted(animal_counts.items())

        print("List " + str(test_number) + ":")

        for i, v in sorted_animal_counts:
            print(i + " | " + str(v))

        test_number += 1

test_input = [
    "List 1:",
    7,
    "bear",
    "tiger",
    "tiger",
    "lion",
    "lion",
    "lion",
    "panther",
    "List 2:",
    4,
    "lion",
    "tiger",
    "bear",
    "horse",
    0
]

count_animals(test_input)