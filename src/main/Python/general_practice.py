import timeit


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]

    return None


def two_sum2(nums, target):
    assist = set()
    for i in range(len(nums)):
        assist.add(nums[i])
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]
            if nums[j] not in assist and nums[i] + nums[j] == target:
                return [i, j]

    return None


def two_sum3(nums, target):
    """
    Time: O(n) run
    Space: O(n) space-complexity
    :param nums: a list of integers
    :param target: lookup value
    :return: indexes of two item that sum-up to 'target
    """
    assist = []
    for i in range(len(nums)):
        assist.append(target - nums[i])
        if target - nums[i] in nums:
            idx = nums.index(target - nums[i])
            if i != idx:
                return [i, idx]

    return None


print("\n***** time-of-first-method ******")
print(timeit.timeit(str(print(two_sum([1, 11, 1, 11, 1, 2, 2, 2, 2, 44], 4)))))

print("\n***** time-of-second-method ******")
print(timeit.timeit(str(print(two_sum2([1, 11, 1, 11, 1, 2, 2, 2, 2, 44], 4)))))

print("\n***** time-of-third-method ******")
print(timeit.timeit(str(print(two_sum3([1, 11, 1, 11, 1, 2, 2, 2, 2, 44], 4)))))

