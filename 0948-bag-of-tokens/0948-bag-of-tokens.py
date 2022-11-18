class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        queue = deque(sorted(tokens))
        score, max_score = 0, 0 
        
        
        while queue:
            if power >= queue[0]:
                t = queue.popleft()
                power -= t
                score += 1
                max_score = max(score, max_score)
            elif score > 0:
                t = queue.pop()
                power += t
                score -= 1
            
            else: 
                break
                
        return max_score
                
        
        