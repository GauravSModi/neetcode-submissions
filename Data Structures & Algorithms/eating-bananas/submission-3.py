class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # - h / len(piles) = avg time to eat 1 pile 
        # - Given that h will always be >= number of piles, the upper bound for k should be the number bananas
        #   in the biggest pile --- max(piles)
        # - If we had  h == total num bananas in the all piles, k would be equal to 1
        # - So k will be: 1 <= k <= max(piles)
        # - Now we want to reduce that until we get the minimum integer k such that you can eat all the bananas
        #   in <= h hours

        if h == len(piles):
            return max(piles)
        
        # 1. find largest pile
        # 2. binary search through it
        # 3. at each interval, iterate through all piles and divide to get num of hours it will take to go through that pile
        # 4. add all of the hours up. if the hours is more than h, k should be higher. if the total hours is more
        #    k should be lower

        r = max(piles) #bigboi pile
        l = 1
        k = 0

        while l <= r:
            # get the mid
            mid = l + ((r-l)//2)

            # now we use this midpoint as the temporary k
            totalTime = 0
            print('round', mid)
            for pile in piles:
                if pile % mid == 0:
                    totalTime += pile // mid
                    print((pile // mid))
                else:
                    totalTime += (pile // mid) + 1
                    print((pile // mid) + 1)

            if totalTime > h: # if it's taking too long to eat all the bananas, increase k
                l = mid+1
            else: # if there was time left over after finishing all the bananas, we can try lowering the k a bit
                r = mid-1
                k = mid

        return k