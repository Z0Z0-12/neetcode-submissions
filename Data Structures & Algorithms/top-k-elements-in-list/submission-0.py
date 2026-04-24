class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        output = []
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        for j in range(k):
            high = max(freq, key = freq.get)
            output.append(high)
            del freq[high]

        return output
