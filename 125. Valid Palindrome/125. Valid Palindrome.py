class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        # Step 1: Remove non-alphanumeric characters and convert to lowercase
        for ch in s:
            if ch.isalnum():
                filtered = filtered + ch.lower()

        # Step 2: Reverse the string
        reversed_string = filtered[::-1]
        # Step 3: Compare original and reversed strings
        if filtered == reversed_string:
            return True
        else:
            return False
        