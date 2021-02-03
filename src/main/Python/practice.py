def two_max_int(height):
    highest_container = 0
    for i in range(len(height)):
        distance = max(i, len(height) - i - 1)
        if height[i] * distance > highest_container:
            highest_container = height[i] * distance

    return highest_container


def max_area(height):
    highest_container = 0
    for i in range(len(height)):
        for j in range(len(height)):
            if i != j and height[j] >= height[i] and \
                    height[i] * abs(j - i) > highest_container:
                highest_container = height[i] * abs(j - i)

    return highest_container


def max_area2(height):
    i, j = 0, len(height) - 1
    water = 0
    while i < j:
        water = max(water, (j - i) * min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return water


l = [1, 8, 6, 2, 5, 14, 8, 3, 7, 8]
l2 = [1,2,1]
print(max_area2(l2))
