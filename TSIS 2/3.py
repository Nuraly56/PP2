class Solution:
    def numIdenticalPairs(self, nums):
        sum = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j: 
                    sum += 1
        return sum