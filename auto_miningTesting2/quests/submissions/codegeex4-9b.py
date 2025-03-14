def max_experience(n, v, c, quests):
    # Sort quests based on the target difficulty level d ascending and XP x descending
    quests.sort(key=lambda q: (q[1], -q[0]))
    
    # Initialize current experience points and level
    current_xp = 0
    current_level = 0
    
    total_xp = 0
    quest_order = []
    
    # Process each quest in the sorted order
    for x, d in quests:
        if current_level >= d:
            # No multiplier applied if at or above target difficulty level
            reward = x
        else:
            # Multiplier applies if below target difficulty level
            reward = c * x
        
        # Add XP from completing the quest
        total_xp += reward
        current_xp += reward
        
        # Check if reaching a new level
        while current_xp >= v:
            current_xp -= v
            current_level += 1
    
    return total_xp

# Input reading
n, v, c = map(int, input().split())
quests = []
for _ in range(n):
    x, d = map(int, input().split())
    quests.append((x, d))

# Calculate and print the maximum experience points
print(max_experience(n, v, c, quests))