class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord('a')] += 1

            result[tuple(count)].append(s)

        return list(result.values())