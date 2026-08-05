class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 1:
            return []

        for n in range(len(nums)):
            for m in range(len(nums)):
                if (n != m) and (nums[n] + nums[m]) == target:
                    return [n, m]
        
        return []
