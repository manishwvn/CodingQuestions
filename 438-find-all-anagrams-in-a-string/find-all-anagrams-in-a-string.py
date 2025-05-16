class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        n, m = len(s), len(p)
        if n < m:
            return []

        p_count = Counter(p)
        s_count = Counter()
        res = []

        for i in range(n):
            s_count[s[i]] += 1

            if i >= m:
                s_count[s[i - m]] -= 1
                if s_count[s[i - m]] == 0:
                    del s_count[s[i - m]]

            if i >= m - 1 and s_count == p_count:
                res.append(i - m + 1)

        return res



        