class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        total = 1

        for i in range(len(nums)):
            if nums[i] != 0:
                total *= nums[i]
            else:
                zero_count += 1
        
        if zero_count >= 2:
            return [0] * len(nums)
        elif zero_count == 0:
            return [int(total/n) for n in nums]
        else:
            ls = [0] * len(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    ls[i] = total
            return ls