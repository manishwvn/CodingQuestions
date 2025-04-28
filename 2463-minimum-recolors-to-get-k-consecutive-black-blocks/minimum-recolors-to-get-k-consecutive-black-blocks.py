class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        # queue = deque()
        # whites = 0

        # for i in range(k):
        #     if blocks[i] == "W":
        #         whites += 1
        #     queue.append(blocks[i])

        # res = whites

        # for i in range(k, len(blocks)):

        #     if queue.popleft() == "W":
        #         whites -= 1

        #     if blocks[i] == "W":
        #         whites += 1
        #     queue.append(blocks[i])

        #     res = min(whites, res)

        # return res

        whites = 0
        res = float("inf")
        l = 0
        for r in range(len(blocks)):
            if blocks[r] == "W":
                whites += 1

            if r - l + 1 == k:
                res = min(res, whites)
                if blocks[l] == "W":
                    whites -= 1
                l += 1

        return res






            
            
        