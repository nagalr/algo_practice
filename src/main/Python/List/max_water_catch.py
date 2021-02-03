def max_area(height):
    highest_container = 0
    for i in range(len(height)):
        for j in range(len(height)):
            if i != j and height[j] >= height[i] and \
                    height[i] * abs(j - i) > highest_container:
                highest_container = height[i] * abs(j - i)

    return highest_container


def max_area2(height):
    """
    Time O(n) run
    Space O(1) not using accessory structure
    :param height: a list
    :return: max water capacity between two lines
    """
    i, j = 0, len(height) - 1
    max_capacity = 0
    while i < j:
        max_capacity = max(max_capacity, (j - i) * min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return max_capacity


l = [1, 8, 6, 2, 5, 14, 8, 3, 7, 8]
l2 = [1, 2, 1]
l3 = [1, 8, 6, 2, 5]
l4 = [6, 9, 3, 4, 5, 8]

print(max_area2(l4))
