def problem_set_solution():
    N = int(input().strip())
    for _ in range(N):
        MAX_SPEED = float(input().strip())
        BICYCLE_SPEED = float(input().strip())
        DISTANCE = float(input().strip())
        START_TIME = float(input().strip())

        time_to_cross_road = 10 / MAX_SPEED
        distance_of_bike_from_dash_line = BICYCLE_SPEED * START_TIME
        distance_of_bike_from_finish_line = DISTANCE - distance_of_bike_from_dash_line
        
        if  BICYCLE_SPEED > 0 and (distance_of_bike_from_finish_line / BICYCLE_SPEED) < time_to_cross_road:
            print("Max beats the first bicycle")
        else:
            time_to_next_bike_arrival = (4 / BICYCLE_SPEED)
            collided_with = (time_to_cross_road - (distance_of_bike_from_finish_line / BICYCLE_SPEED)) // time_to_next_bike_arrival + 1
            
            if collided_with < 1 or collided_with > 10:
                print("Max crosses safely after bicycle", str(int(collided_with)))
            else:
                print("Collision with bicycle", str(int(collided_with)))

problem_set_solution()                