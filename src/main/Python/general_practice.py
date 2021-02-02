def two_sum(nums, target):
    result = set()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                result.add(i)
                result.add(j)
                return result

    return result


def two_sum2(nums, target):
    assist = set()
    for i in range(len(nums)):
        assist.add(nums[i])
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]
            elif nums[j] not in assist and nums[i] + nums[j] == target:
                return [i, j]

    return None


print(two_sum2([1, 2, 2, 4], 6))
