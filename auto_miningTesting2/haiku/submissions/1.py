def decompose(word, syllables, memo):
    if word in memo: 
        return memo[word]
    if word in syllables:
        memo[word] = [len(word)]
    else:
        memo[word] = []
        for i in range(1, len(word)):
            left = word[:i]
            right = word[i:]
            if right in syllables:
                left_decomp = decompose(left, syllables, memo)
                for ld in left_decomp:
                    memo[word].append(ld + len(right))
    return memo[word]

def check_haiku(syllables, poem):
    memo = {}
    for line in poem:
        syllables_in_line = sum(len(decompose(word, syllables, memo)) for word in line.split())
        if syllables_in_line != 5 and syllables_in_line != 7:
            return 'come back next year'
    return 'haiku'

S = int(input())
syllables = set(input().split())
poem = [input() for _ in range(3)]
print(check_haiku(syllables, poem))