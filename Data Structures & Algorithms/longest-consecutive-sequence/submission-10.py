class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        print(nums)
        longest = 0
        ls = []

        for i in range(len(nums)):
            if ls == [] or nums[i] - 1 == nums[i-1]:
                ls.append(nums[i])
                if len(ls) > longest:
                    longest = len(ls)
            else:
                ls.clear()
                ls.append(nums[i])
        return longest