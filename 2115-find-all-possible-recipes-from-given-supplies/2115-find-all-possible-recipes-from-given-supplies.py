class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
    
        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])

        print(graph)

        counter = defaultdict(int)

        for i in range(len(recipes)):
            counter[recipes[i]] = len(ingredients[i])

        print(counter)

        queue = deque()
        for i in range(len(supplies)):
            queue.append(supplies[i])

        result = []
        # visited = set()

        while queue:
            curr = queue.popleft()
            
            if curr in counter:
                result.append(curr)
            
            if curr in graph:
                for recipe in graph[curr]:
                    # if recipe not in visited:
                    counter[recipe] -= 1
                    if counter[recipe] == 0:
                        # result.append(recipe)
                        # visited.add(recipe)
                    
                        queue.append(recipe)

        return result
