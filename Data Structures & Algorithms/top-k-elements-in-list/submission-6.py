class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        for x in range(k):
            mostF = max(hashmap, key = hashmap.get)
            res.append(mostF)
            del hashmap[mostF]
        
        return res