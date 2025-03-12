def calculate_optimal_speed(beginner_count, normal_count, expert_count, beginner_strength, normal_strength, expert_strength, canoe_speeds):
  """
  Calculates the maximum possible speed of the slowest canoe.

  Args:
    beginner_count: The number of beginner paddlers.
    normal_count: The number of normal paddlers.
    expert_count: The number of expert paddlers.
    beginner_strength: The strength of a beginner paddler.
    normal_strength: The strength of a normal paddler.
    expert_strength: The strength of an expert paddler.
    canoe_speeds: A list of speed factors for each canoe.

  Returns:
    The maximum possible speed of the slowest canoe.
  """

  total_paddlers = beginner_count + normal_count + expert_count
  canoe_count = total_paddlers // 2

  # Sort canoe speeds in ascending order
  canoe_speeds.sort()

  # Calculate the combined strength of all possible pairs
  combined_strengths = []
  
  # All possible expert pairs
  for i in range(expert_count // 2):
    combined_strengths.append(2 * expert_strength)

  # Pair remaining experts with beginners (if any)
  remaining_experts = expert_count % 2
  for i in range(min(remaining_experts, beginner_count)):
    combined_strengths.append(expert_strength + beginner_strength)

  # Pair remaining experts with normal paddlers (if any)
  remaining_experts -= min(remaining_experts, beginner_count)
  for i in range(min(remaining_experts, normal_count)):
    combined_strengths.append(expert_strength + normal_strength)

  # All possible normal pairs
  for i in range(normal_count // 2):
    combined_strengths.append(2 * normal_strength)

  # Pair remaining normals with beginners (if any)
  remaining_normals = normal_count % 2
  for i in range(min(remaining_normals, beginner_count)):
    combined_strengths.append(normal_strength + beginner_strength)

  # All possible beginner pairs
  for i in range(beginner_count // 2):
    combined_strengths.append(2 * beginner_strength)

  # Sort combined strengths in descending order to prioritize slower canoes
  combined_strengths.sort(reverse=True)

  # Calculate the minimum speed among all canoes
  min_speed = float('inf')
  for i in range(canoe_count):
    speed = canoe_speeds[i] * combined_strengths[i]
    min_speed = min(min_speed, speed)

  return int(min_speed)  # Return the speed as an integer


# Read input values
beginner_count, normal_count, expert_count = map(int, input().split())
beginner_strength, normal_strength, expert_strength = map(int, input().split())
canoe_speeds = list(map(int, input().split()))

# Calculate and print the maximum speed of the slowest canoe
max_min_speed = calculate_optimal_speed(beginner_count, normal_count, expert_count, beginner_strength, normal_strength, expert_strength, canoe_speeds)
print(max_min_speed)
