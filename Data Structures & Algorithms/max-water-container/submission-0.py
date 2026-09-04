class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights)-1

        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            curr = h * w
            maxArea = max(curr, maxArea)

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l+= 1
        
        return maxArea