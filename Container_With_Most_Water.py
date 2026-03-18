class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        currArea = 0
        mArea = 0

        while left < right:
            
            currArea = min(height[left], height[right]) * (right - left)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

            if mArea < currArea:
                mArea = currArea

        return mArea