def calculate_probability(num_buses, num_stations, deadline, bus_data):
    """
    Calculates the maximum probability of reaching the airport on time.

    Args:
        num_buses: The number of buses.
        num_stations: The number of stations.
        deadline: The time by which you must arrive at the airport.
        bus_data: A list of tuples representing bus information. 
                   Each tuple contains (start_station, destination_station, departure_time, arrival_time, probability).

    Returns:
        The maximum probability of reaching the airport on time.
    """

    # dp[i][j] represents the maximum probability of reaching station j at time i
    dp = [[0.0 for _ in range(num_stations)] for _ in range(deadline + 1)]
    dp[0][0] = 1.0  # Initial state: At time 0, probability at station 0 is 1

    for time in range(deadline):
        for current_station in range(num_stations):
            if dp[time][current_station] > 0:
                for bus_index in range(num_buses):
                    start_station, dest_station, dep_time, arr_time, prob = bus_data[bus_index]
                    
                    # If the bus departs from the current station at the current time
                    if start_station == current_station and dep_time == time:
                        # Update the probability of reaching the destination station
                        dp[arr_time][dest_station] = max(
                            dp[arr_time][dest_station],
                            dp[time][current_station] * prob
                        )

                # Consider staying at the current station for the next time unit
                dp[time + 1][current_station] = max(
                    dp[time + 1][current_station],
                    dp[time][current_station]
                )
    
    return dp[deadline][1]  # Probability of being at the airport (station 1) by the deadline


if __name__ == "__main__":
    num_buses, num_stations = map(int, input().split())
    deadline = int(input())
    buses = []

    for _ in range(num_buses):
        a, b, s, t, p = map(float, input().split())
        buses.append((int(a), int(b), int(s), int(t), p))

    probability = calculate_probability(num_buses, num_stations, deadline, buses)
    print(f"{probability:.6f}")