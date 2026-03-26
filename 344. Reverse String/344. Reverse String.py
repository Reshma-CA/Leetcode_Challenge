from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        new_str =  "".join(s)
        rev_str = ""
        for item in new_str:
            rev_str = item + rev_str
        s[:] = list(rev_str)
        