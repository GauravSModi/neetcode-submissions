class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        l, r = 0, len(heights)-1

        while l < r:
            vol = (r-l) * (min(heights[l], heights[r]))

            if vol > maxWater:
                maxWater = vol
            
            if heights[l] >= heights[r]:
                r-=1
            else:
                l+=1
            
        return maxWater