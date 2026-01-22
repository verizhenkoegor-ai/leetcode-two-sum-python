class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            need = target - nums[i]

            if need in seen:
                return [seen[need], i]

            seen[nums[i]] = i

[2,7,11,15]
9
[3,2,4]
6
[3,3]
6

Input
nums =
[2,7,11,15]
target =
9
Output
[0,1]
Expected
[0,1] 
