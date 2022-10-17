class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n = len(costs) // 2
        diff = []
        for city_a, city_b in costs:
            diff.append([city_b - city_a, city_a, city_b])
            
        diff.sort()
        res = 0
        
        for i in range(2*n):
            if i < n:
                res += diff[i][2]
                
            else:
                res += diff[i][1]
                
        return res
        
            
        