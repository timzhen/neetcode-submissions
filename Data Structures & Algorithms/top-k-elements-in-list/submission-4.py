class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        hashtable = {}

        for n in nums:
            hashtable[n] = hashtable.get(n,0) + 1
        
        while k > 0:
            maxFreq = max(hashtable, key = hashtable.get)
            result.append(maxFreq)
            del hashtable[maxFreq]
            k -= 1

        return result