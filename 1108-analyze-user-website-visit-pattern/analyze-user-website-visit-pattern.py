class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        g = defaultdict(list)

        for (t, user, web) in sorted(zip(timestamp, username, website)):
            g[user].append(web)

        scores = defaultdict(int)
        for user, websites in g.items():
            for pattern in set(itertools.combinations(websites, 3)):
                scores[pattern] += 1
        
        max_pattern, max_cnt = '', 0
        for pattern, cnt in scores.items():
            if cnt > max_cnt or (cnt == max_cnt and pattern < max_pattern):
                max_pattern = pattern
                max_cnt = cnt

        return max_pattern