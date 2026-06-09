# https://leetcode.com/problems/two-sum/description/


def twoSum(nums, target):
    if not nums: return []

    hashdict = {}  # init hash, key is number needed to complete the value.

    for i, val in enumerate(nums):
        if hashdict.get(val) is not None: return [hashdict[val], i]

        else: hashdict.update({target - val: i})

    return []


print(twoSum([2, 7, 11, 15], 9))

