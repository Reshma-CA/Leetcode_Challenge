class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_str = str(x)
        new_str2 = new_str[::-1]
        if new_str == new_str2:
            return True
        else:
            return False 

    # or

    class Solution1:
        def isPalindrome1(self, x: int) -> bool:
            # Convert to string and compare with its reverse
            return str(x) == str(x)[::-1]