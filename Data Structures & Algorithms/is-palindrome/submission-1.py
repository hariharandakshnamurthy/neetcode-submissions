import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized = ''.join(re.split(r'\W+', s)).lower()
        reversed = normalized[::-1]
        if normalized == reversed:
            return True
        else:
            return False

        