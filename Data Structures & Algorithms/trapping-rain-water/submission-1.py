# My initial idea was to get the maxHeight. Until the left pointer arrived to the max height, 
# it would be the lower bar and we could calculate the amount of rain water at bar by using that.
# After that, we could find the next tallest, and then the next tallest, until getting to the end.
# But that means we have to keep combing the array for the next max
# this means this algorithm is at best O (nlogn)... (if we sort the array)
# Fuck...
# However...
# we can make it O(n) by calculating prefix max (max on the left side for each element) 
# and suffix max (max on the right side of each element) initially

class Solution:
    def trap(self, height: List[int]) -> int:
        maxVol = 0
        prefix = [0]*len(height)
        postfix = [0]*len(height)
        res = [0] * len(height)

        l, r = 0, len(height) - 1
        premax, postmax = 0, 0  # keep it 0 to start off because you don't want the edge bars to be counted anyways
        
        while l < len(height):
            prefix[l] = premax
            postfix[r] = postmax

            if height[l] > premax:
                premax = height[l]
            if height[r] > postmax:
                postmax = height[r]
                
            l+=1
            r-=1

        for i, x in enumerate(height):
            minbar = min(prefix[i], postfix[i])
            if minbar > x:
                maxVol += minbar - x
        
        return maxVol