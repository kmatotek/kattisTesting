def check_collision(max_speed, cyclist_speed, distance, start_time):
    max_diameter = 1.0
    road_width = 10.0
    bike_length = 2.0
    bike_space = 2.0
    
    # Calculate the time it takes for Max to cross the road
    crossing_time = road_width / max_speed
    
    if start_time >= crossing_time:
        return "Max beats the first bicycle"
    
    # Calculate relative speed and distance
    relative_speed = cyclist_speed - max_speed
    initial_distance_to_first_bicycle = distance + bike_space
    
    # Time to reach the first bicycle
    time_to_reach_first_bicycle = initial_distance_to_first_bicycle / relative_speed
    
    if time_to_reach_first_bicycle <= crossing_time:
        return f"Collision with bicycle 1"
    
    # Check collision with subsequent bicycles
    for k in range(2, 11):
        distance_to_current_bicycle = initial_distance_to_first_bicycle + (k - 1) * bike_space * 2
        time_to_reach_current_bicycle = distance_to_current_bicycle / relative_speed
        
        if time_to_reach_current_bicycle <= crossing_time:
            return f"Collision with bicycle {k}"
    
    return "Max crosses safely after bicycle 9"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(N):
        M = float(data[index])
        B = float(data[index + 1])
        D = float(data[index + 2])
        T = float(data[index + 3])
        index += 4
        
        result = check_collision(M, B, D, T)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()