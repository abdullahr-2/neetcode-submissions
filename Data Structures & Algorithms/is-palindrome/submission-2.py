class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([element for element in list(s) if element.isalnum()]).lower()

        return s == s[::-1]