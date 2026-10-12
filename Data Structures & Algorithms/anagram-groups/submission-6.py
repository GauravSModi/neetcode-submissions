class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            sortedS = ''.join(sorted(s))

            if sortedS in seen:
                seen[sortedS].append(s)
            else:
                seen[sortedS] = [s]

        
        res = list(seen.values())

        return res