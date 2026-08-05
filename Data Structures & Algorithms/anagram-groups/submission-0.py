class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for n in s:
                count[ord(n) - ord('a')] += 1 
                # finds a ... z and increases total by 1
            hashmap[tuple(count)].append(s)
        
        return list(hashmap.values())

