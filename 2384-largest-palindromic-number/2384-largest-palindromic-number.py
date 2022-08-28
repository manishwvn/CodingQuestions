class Solution:
    def largestPalindromic(self, num: str) -> str:
        digit_freq = [0] * 10
        res = ""
        for n in num:
            digit_freq[int(n)] += 1
            
        for i in range(10):
            while(digit_freq[i] >= 2):
                res += str(i)
                res = str(i) + res
                digit_freq[i] -= 2
        for i in reversed(range(10)):
            if digit_freq[i] > 0:
                mid = int(len(res)/2)
                res = res[:mid] + str(i) + res[mid:]
                break
            
        res = res.strip('0')
        return res if res != "" else "0"