class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        if not costs or len(costs) == 0:
            return 0
    
        previous = costs[-1]
    
        for i in range(len(costs)-2, -1, -1):
            current = deepcopy(costs[i])
            current[0] += min(previous[1], previous[2])
            current[1] += min(previous[0], previous[2])
            current[2] += min(previous[0], previous[1])
            previous = current

        return min(previous)
        
        
        