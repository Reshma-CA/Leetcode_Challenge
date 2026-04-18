class Solution:
    def reverseWords(self, s: str) -> str:
        split_str =s.split()
        left = 0
        right = len(split_str)-1
        while(left<right):
            split_str[left],split_str[right] = split_str[right],split_str[left]
            left+=1
            right-=1
        return " ".join(split_str)
        