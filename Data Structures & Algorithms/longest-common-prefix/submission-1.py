class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lp = strs[0]

        for s in strs:
            if len(lp) > len(s):
                lp = lp[:len(s)]
            else:
                s = s[:len(lp)]

            while s != lp:
                lp = lp[:-1]
                s = s[:-1]

        return lp