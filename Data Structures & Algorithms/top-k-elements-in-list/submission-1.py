class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = dict()

        for n in nums:
            if n in hash.keys():
                hash[n] += 1
            else:
                hash[n] = 1

        return sorted(hash, key=hash.get, reverse=True)[:k]
        