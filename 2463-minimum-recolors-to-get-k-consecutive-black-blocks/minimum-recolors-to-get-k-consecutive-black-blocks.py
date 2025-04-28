class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        queue = deque()
        whites = 0

        for i in range(k):
            if blocks[i] == "W":
                whites += 1
            queue.append(blocks[i])

        res = whites

        for i in range(k, len(blocks)):

            if queue.popleft() == "W":
                whites -= 1

            if blocks[i] == "W":
                whites += 1
            queue.append(blocks[i])

            res = min(whites, res)

        return res




            
            
        