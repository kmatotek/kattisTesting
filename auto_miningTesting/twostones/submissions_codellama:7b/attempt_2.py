n = int(input())
alice_count, bob_count = 0, 0
while n > 1:
    if n % 2 == 0 and n >= 3:
        n -= 2
        alice_count += 1
    else:
        n -= 2
        bob_count += 1
if alice_count > bob_count:
    print("Alice")
else:
    print("Bob")