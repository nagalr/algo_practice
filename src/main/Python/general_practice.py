import time


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
            elif nums[j] not in assist and nums[i] + nums[j] == target:
                return [i, j]

    return None


# compare the running times of the two methods
print("***** tme-of-first-method ******")
t1 = time.time()
print(two_sum([1, 2, 2, 4, 5, 7, 8, 9, 10], 6))
t2 = time.time()
print("The time of the first is: " + str((t2 - t1) * 10000))

print("\n***** tme-of-second-method ******")
t3 = time.time()
print(two_sum2([1, 2, 2, 4, 5, 7, 8, 9, 10], 6))
t4 = time.time()
print("The time of the first is: " + str((t4 - t3) * 10000))
