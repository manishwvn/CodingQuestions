from collections import deque

class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q:
            return 0

        graph = {}
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.val not in graph:
                graph[node.val] = []

            if node.left:
                graph[node.val].append(node.left.val)

                if node.left.val not in graph:
                    graph[node.left.val] = []
                graph[node.left.val].append(node.val)

                queue.append(node.left)

            if node.right:
                graph[node.val].append(node.right.val)

                if node.right.val not in graph:
                    graph[node.right.val] = []
                graph[node.right.val].append(node.val)

                queue.append(node.right)

        visited = set([p])
        queue = deque([[p, 0]])

        while queue:
            node, dist = queue.popleft()

            if node == q:
                return dist

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append([neighbor, dist + 1])

        return -1