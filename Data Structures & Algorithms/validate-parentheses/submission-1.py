class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c_bracket = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for b in s:
            if b not in c_bracket.keys():
                stack.append(b)
            else:
                if not stack or stack.pop() != c_bracket[b]:
                    return False

        if stack:
            return False
        else:
            return True