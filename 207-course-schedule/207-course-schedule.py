class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hm = collections.defaultdict(list)
        ind = [0] * numCourses
        
        for req in prerequisites:
            ind[req[0]] += 1
            
            if req[1] not in hm:
                hm[req[1]] = []
                
            hm[req[1]].append(req[0])
            
        
        q = collections.deque()
        count = 0
        
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)
                count += 1
           
        if count == numCourses:
            return True
        
        while q:
            curr = q.popleft()
            children = hm[curr]
            
            if children:
                for child in children:
                    ind[child] -= 1
                    
                    if ind[child] == 0:
                        q.append(child)
                        count += 1
                        if count == numCourses:
                            return True
                        
        return False
                    
            
        
                
        
        