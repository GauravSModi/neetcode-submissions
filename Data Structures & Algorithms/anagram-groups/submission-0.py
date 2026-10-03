class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # o(n^2) when you check anagram for each word against every other word
        # o(n) when you sort and use dictionary? technically o(n * klogk), where n is num words, and k is length of words
        anagrams = {}

        for i, s in enumerate(strs):
            curr = ''.join(str(x) for x in sorted(s))
            if curr in anagrams:
                anagrams[curr].append(i)
                print(anagrams[curr])
            else:
                anagrams[curr] = [i]
            
        final = []

        for vals in anagrams.values():
            curr = []
            for i in vals:
                curr.append(strs[i])
            final.append(curr)
        
        return final