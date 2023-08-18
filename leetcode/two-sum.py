# https://leetcode.com/problems/two-sum/


def twoSum_firsttry(nums, target):
    for index1, i in enumerate(nums):
        for index2, j in enumerate(nums):
            if i + j == target and index1 != index2:
                return [index1, index2]


def twoSum_optimised(nums, target):
    for i in range(len(nums)-1):
        for index, j in enumerate(nums[i+1:]):
            if nums[i] + j == target:
                return [i, index]

test = twoSum_optimised([3,2,4], 6)
