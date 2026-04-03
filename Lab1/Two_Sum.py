class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        curr = 0
        while left < right:
            curr = nums[left] + nums[right]
            if (curr) == target:
                return [left, right]
            elif right - 1 > left:
                right -= 1
            else:
                right = len(nums) - 1
                left += 1
