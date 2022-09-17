"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        hm = {}
        
        for emp in employees:
            hm[emp.id] = emp
            
        queue = deque()
        queue.append(id)
        result = 0
        while queue:
            eid = queue.popleft()
            emp = hm[eid]
            result += emp.importance
            for sub in emp.subordinates:
                queue.append(sub)
                
        return result
            
            
            
        
        