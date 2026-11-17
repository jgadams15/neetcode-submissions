class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap called count
        # count how many of each letter they have
        # for eat:
        # key will be e a t
        # value in hashmap with be the list of words that are an anagram
        # [eat, tea, ate]
        res = defaultdict(list) # mapping the charCount to list of Anagrams

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return list(res.values())