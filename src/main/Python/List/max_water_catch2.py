def trap(height):
    """
    Time O(n) run
    :param height: a list
    :return: max water capacity
    """
    max_left = 0
    max_right = 0
    capacity = 0

    for i in range(len(height)):
        if height[:i]:
            max_left = max(height[:i])
        if height[i:]:
            max_right = max(height[i:])

        max_neighbor = min(max_left, max_right)

        if max_neighbor - height[i] > 0:
            capacity += max_neighbor - height[i]

    return capacity


height = [4, 2, 0, 3, 2, 5]
height2 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height2))
