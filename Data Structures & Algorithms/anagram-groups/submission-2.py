class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []


        for curr_word in strs:
            found = False
            dict1 = {}
            for char in curr_word:
                if not char in dict1:
                    dict1[char] = 1
                else:
                    dict1[char] += 1

            for anagram_list in anagrams:
                if found:
                    continue

                anagram = anagram_list[0]

                if len(curr_word) != len(anagram):
                    continue
                

                dict2 = {}

                for char in anagram:
                    if not char in dict2:
                        dict2[char] = 1
                    else:
                        dict2[char] += 1
                        
                if dict1 == dict2:
                    found = True
                    anagram_list.append(curr_word)

            if not found:
                anagrams.append([curr_word])

        return anagrams
