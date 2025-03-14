def count_syllables(word):
    vowels = "aeiou"
    syllable_count = 0
    in_vowel_group = False
    
    for char in word:
        if char.lower() in vowels:
            if not in_vowel_group:
                syllable_count += 1
                in_vowel_group = True
        else:
            in_vowel_group = False
    
    return syllable_count

def decompose_word(word, syllables):
    def backtrack(start, path):
        if start == len(word) and len(path) == len(syllables):
            result.append(list(path))
        elif start < len(word) and len(path) < len(syllables):
            for i in range(1, min(len(word) - start + 1, 8)):
                current_syllable = word[start:start+i]
                if count_syllables(current_syllable) <= syllables[len(path)]:
                    backtrack(start + i, path + [current_syllable])
    
    result = []
    backtrack(0, [])
    return result

def is_haiku(poem_lines, syllables):
    total_syllables = sum(syllables)
    if total_syllables != len(poem_lines[0]) + len(poem_lines[1]) + len(poem_lines[2]):
        return False
    
    def backtrack(line_index, remaining_syllables, words_used):
        if line_index == 3:
            return True
        
        for decomposition in decompositions[line_index]:
            if sum(count_syllables(word) for word in decomposition) <= remaining_syllables:
                if is_haiku(poem_lines, [remaining_syllables - sum(count_syllables(word) for word in decomposition)] + syllables[1:]):
                    return True
        return False
    
    decompositions = [decompose_word(line, [syllables[0], syllables[1]]) for line in poem_lines[:3]]
    return backtrack(0, total_syllables, set())

def main():
    S = int(input())
    syllables = list(map(int, input().split()))
    
    poem_lines = []
    for _ in range(3):
        poem_lines.append(list(input().split()))
    
    if is_haiku(poem_lines, syllables):
        print("haiku")
    else:
        print("come back next year")

if __name__ == "__main__":
    main()