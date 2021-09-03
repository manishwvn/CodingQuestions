class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        n = len(routes)
        
        hm = {}
        
        for i in range(n):
            for j in range(len(routes[i])):
                
                busStop = routes[i][j]
                if busStop in hm:
                    busNum = hm[busStop]
                else:
                    busNum = []
                    
                busNum.append(i)
                hm[busStop] = busNum
                
        
        queue = []
        busStopVis = {}
        busVis = {}
        level = 0
        
        queue.append(source)
        busStopVis[source] = 1
        
        while(queue):
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)

                if node == target:
                    return level

                buses = hm[node]

                for bus in buses:
                    if bus in busVis:
                        continue

                    arr = routes[bus]

                    for busStop in arr:
                        if busStop in busStopVis:
                            continue

                        queue.append(busStop)
                        busStopVis[busStop] = 1

                    busVis[(bus)] = 1
                        
            level += 1
            
            
        return -1