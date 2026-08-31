import string
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = s.replace(" ", "")
        punc = f"[({re.escape(string.punctuation)})]"
        clean = re.sub(punc, "", n)
        clean = clean.lower()

        if clean == clean [::-1]:
            return True
        return False