class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([element for element in list(s) if element.isalnum()]).lower()

        if s == s[::-1]:
            return True
        else:
            return False