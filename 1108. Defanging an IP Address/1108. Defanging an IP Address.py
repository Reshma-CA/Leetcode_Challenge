class Solution:
    def defangIPaddr(self, address: str) -> str:
        str1 = address.split('.')
        result = '[.]'.join(str1)
        return result

#or

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")   