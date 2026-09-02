class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        chars = []
        longest = 0

        while r < len(s):
            c = s[r]
            chars.append(c)
            
            if c in chars[:-1]:
                chars = chars[chars.index(c) + 1:]
            
            longest = max(longest, len(chars))
            r += 1
        
        return longest
