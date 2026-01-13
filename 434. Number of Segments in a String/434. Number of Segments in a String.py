class Solution:
    def countSegments(self, s: str) -> int:
        return len([seg for seg in s.split(" ") if seg]) # empty string is ignored(if seg)
        