class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i, n in enumerate(nums):
            dif = target - n
            if dif in h:
                return [h[dif], i]
            h[n] = i