class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        list_1, list_2 = s1.split(' '), s2.split(' ')
        set_1, set_2 = Counter(list_1), Counter(list_2)

        result = []
        for word, count in set_1.items():
            if word not in set_2 and count == 1:
                result.append(word)
        for word, count in set_2.items():
            if word not in set_1 and count == 1:
                result.append(word)
        return result

        