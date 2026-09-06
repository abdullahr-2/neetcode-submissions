class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        return nums.index(target)
        # index = 0
        
        # while True:
        #     n = len(nums)
        #     middle = (n // 2)
        #     print(nums)

        #     index += middle

        #     if nums[middle] == target:
        #         return index
        #     elif target > nums[middle]:
        #         nums = nums[middle + 1:]
        #     else:
        #         nums = nums[:middle]