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


print("***** time-of-first-method ******")
print(timeit.timeit(str(print(two_sum([1, 3, 7, 9, 2], 11)))))
print("\n***** time-of-second-method ******")
print(timeit.timeit(str(print(two_sum2([1, 3, 7, 9, 2], 11)))))
