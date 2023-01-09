class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count, seen, stk = Counter(s), {s[0]}, [s[0]]
        for curr in s[1:]:
            if curr in seen:
                count[curr] -=1
                continue

            while stk and count[stk[-1]] > 1 and stk[-1] > curr:                
                seen.discard(stk[-1])
                count[stk[-1]] -=1
                stk.pop()

            stk.append(curr)
            seen.add(curr)
                                
        return "".join(stk)