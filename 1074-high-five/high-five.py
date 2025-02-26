class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        scores = defaultdict(list)

        for item in items:
            scores[item[0]].append(item[1])          

        for student, score in scores.items():
            score.sort(reverse=True)
            scores[student] = score[:5]
        
        result = []
        for student, score in scores.items():
            avg = sum(score) // 5
            result.append([student, avg])
        
        result.sort(key = lambda x: x[0])
        return result
        