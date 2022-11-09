class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        counting=haystack.split(needle)
        if len(counting)==1:
            return -1
        return(len(counting[0]))