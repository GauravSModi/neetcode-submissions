import copy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [-2, 3, 4, 5]
        # Prefix: [-2, -6, -24]
        # Postfix: [60, 20, 5]

        l = len(nums)

        prefix = [1] * (l-1)
        postfix = [1] * (l-1)

        for i in range(l-1):
            if i > 0:
                prefix[i] = prefix[i-1] * nums[i]
                postfix[l-i-2] = postfix[l-i-1] * nums[l-i-1]
            else:
                prefix[i] = nums[i]
                postfix[l-i-2] = nums[l-1]
            
        res = [0] * l

        for i in range(l-1):
            if i > 0:
                res[i] = prefix[i-1] * postfix[i]
            else:
                # calculate edges of list
                res[0] = postfix[0]
                res[l-1] = prefix[l-2]

        return res