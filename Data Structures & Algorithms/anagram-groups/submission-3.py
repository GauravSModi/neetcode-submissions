class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for i, s in enumerate(strs):
            sorted_curr = tuple(sorted(s))
            if sorted_curr in anagrams:
                anagrams[sorted_curr].append(i)
            else:
                anagrams[sorted_curr] = [i]
        
        final = []

        for val in anagrams.values():
            curr = []
            for i in val:
                curr.append(strs[i]) 
            
            final.append(curr)
        
        return final