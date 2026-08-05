class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        hashmap = {}

        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1
        
        while k > 0:
            maxFreq = max(hashmap, key = hashmap.get)
            k -= 1
            ans.append(maxFreq)
            hashmap.pop(maxFreq,None)
        return ans