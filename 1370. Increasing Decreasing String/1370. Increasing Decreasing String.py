class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)   # Convert string to list for easy removal
        result = ""
        
        while s:
            # Step 1: Increasing order (a → z)
            for ch in sorted(set(s)):
                s.remove(ch)
                result += ch
            
            # Step 2: Decreasing order (z → a)
            for ch in sorted(set(s), reverse=True):
                s.remove(ch)
                result += ch
        
        return result
        