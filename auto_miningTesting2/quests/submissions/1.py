import heapq
def xp_quests(n, v, c, quests):
    # Initialize variables
    xp = 0
    level = 0
    max_xp = 0
    # Create a min heap of all quests, sorted by the target difficulty level
    quests = sorted([(d,-x) for x, d in quests])
    remaining = []
    
    # Repeat until we have finished all the quests
    while quests or remaining:
        # While we still have quests of the current difficulty level...
        while quests and quests[0][0] <= level:
            (d, minus_x) = heapq.heappop(quests)
            # We push the experience points to the remaining array
            heapq.heappush(remaining, minus_x)
        
        # If we have no quests to complete at the current level, we level up
        if not remaining:
            level = quests[0][0]
        else:
            # Otherwise, we complete a quest
            minus_x = heapq.heappop(remaining)
            xp -= minus_x
            max_xp = max(max_xp, xp)
            # And level up if possible
            while remaining and xp >= (level+1) * v:
                level += 1
                minus_x = heapq.heappop(remaining)
                xp -= minus_x
                max_xp = max(max_xp, xp)
                
    return max_xp