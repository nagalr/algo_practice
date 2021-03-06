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
    Time: O(n^2) run
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
                return [idx, i]

    return None


def two_sum4(nums, target):
    for i in range(len(nums)):
        try:
            idx = nums.index(target - nums[i])
        except:
            continue
        if idx != i:
            return [idx, i]

    return None


def two_sum5(nums, target):
    """
    Time: O(n) run
    Space: add O(n) dictionary structure
    :param nums: a list
    :param target: target value
    :return: two list indices, their list values sum to target
    """
    dict = {}
    values = []

    for i in range(len(nums)):
        if nums[i] in values:
            return [keys[values.index(nums[i])], i]
        else:
            dict[i] = target - nums[i]
            values = list(dict.values())
            keys = list(dict.keys())

    return None


def two_sum6(nums, target):
    dict = {}
    for i in range(len(nums)):
        if nums[i] in dict.keys():
            return [dict[nums[i]], i]
        else:
            dict[target - nums[i]] = i

    return None


if __name__ == "__main__":
    print("\n***** time-of-first-method ******")
    print(timeit.timeit(str(print(two_sum([1, 11, 1, 11, 1, 2, 2, 2, 2, 44], 4)))))

    print("\n***** time-of-second-method ******")
    print(timeit.timeit(str(print(two_sum2([1, 11, 1, 11, 1, 2, 2, 2, 2, 44], 4)))))

    print("\n***** time-of-third-method ******")
    print(timeit.timeit(str(print(two_sum3([1, 11, 1, 11, 1, 2, 2, 2, 2, 44], 4)))))

    print("\n***** time-of-four-method ******")
    print(timeit.timeit(str(print(two_sum4([1, 11, 1, 11, 1, 2, 2, 2, 2, 44], 4)))))

    print("\n***** time-of-five-method ******")
    print(timeit.timeit(str(print(two_sum5([1, 11, 1, 11, 1, 2, 2, 2, 2, 44], 4)))))

    print("\n***** time-of-six-method ******")
    print(timeit.timeit(str(print(two_sum6([1, 11, 1, 11, 1, 2, 2, 2, 2, 44], 4)))))
