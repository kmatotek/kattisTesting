def find_frames(mug_height):
  """
  Finds two frames in the video between which the mug has fallen a distance equal to mug_height.

  Args:
    mug_height: The height of the mug in millimeters.

  Returns:
    A tuple containing the two frame numbers (n1, n2) if they exist, otherwise the string "impossible".
  """

  for frame1 in range(int(mug_height**0.5) + 1):
    for frame2 in range(frame1 + 1, int(mug_height**0.5) + 2):
      distance_fallen = frame2**2 - frame1**2
      if distance_fallen == mug_height:
        return frame1, frame2
  return "impossible"

if __name__ == "__main__":
  distance_to_measure = int(input())
  frame1, frame2 = find_frames(distance_to_measure)
  print(f"{frame1} {frame2}" if frame2 != "impossible" else "impossible")