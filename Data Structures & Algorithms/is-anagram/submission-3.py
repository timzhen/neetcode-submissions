class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        for x in s:
            hash1[x] = hash1.get(x,0) + 1
        for x in t:
            hash2[x] = hash2.get(x,0) + 1
        return hash1 == hash2