class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # make a map/dict
        # one pass
        j_map = {}
        
        for i, x in enumerate(nums):
            remainder = target - x
            if remainder in j_map:
                return [j_map[remainder], i]
            j_map[x] = i
