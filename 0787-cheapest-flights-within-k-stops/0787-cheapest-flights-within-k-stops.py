class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        price_map = defaultdict(lambda: 10**5)
        for i in range(len(flights)):    
            graph[flights[i][0]].append((flights[i][1], flights[i][2]))

        
        price_map[src] = 0
        priority_queue = deque()
        priority_queue.append((0, src, k + 1))

        while priority_queue:
            
            price, node, stops = priority_queue.popleft()
            price_map[node] = min(price_map[node], price)
            
            if node == dst:
                continue
            
            if stops > 0:
                for neigh, cost in graph[node]:
                    
                    if price_map[neigh] < price + cost:
                        continue
                    priority_queue.append((price + cost, neigh, stops - 1))

        if dst not in price_map:
            return -1
        
        return price_map[dst] 
