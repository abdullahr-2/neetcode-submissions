class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            l_height, r_height = heights[l], heights[r]

            tmp = min(l_height, r_height) * (r - l)
            res = tmp if tmp > res else res

            if l_height < r_height:
                l += 1
            elif l_height > r_height:
                r -= 1
            else:
                l += 1
                r -= 1

        return res
            
