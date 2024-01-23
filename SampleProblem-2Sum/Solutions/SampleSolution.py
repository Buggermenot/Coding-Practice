class Solution:
    def twoSum(nums: list, target: int) -> list:
        indices = dict()

        n = len(nums)
        for i in range(n):
            indices[nums[i]] = i+1

        for i in range(n):
            a = target - nums[i]
            if indices.get(a, 0) and indices.get(a, 0) != i+1:
                return [i, indices[a] - 1]
        
        return []