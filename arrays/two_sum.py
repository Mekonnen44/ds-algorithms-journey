def two_sum(nums, target):
    hashmap = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i

    return []

# test
print(two_sum([2,7,11,15], 9))  # [0,1]