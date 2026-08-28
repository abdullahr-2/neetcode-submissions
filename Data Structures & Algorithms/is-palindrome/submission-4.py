class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [element.lower() for element in list(s) if element.isalnum()]
        if s == []:
            return True
        right, left = len(s) - 1, 0

        for i in range((len(s) // 2) + 1):
            if s[right] == s[left]:
                right -= 1
                left += 1
            else:
                return False
        return True