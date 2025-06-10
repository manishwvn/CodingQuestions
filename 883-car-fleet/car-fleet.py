class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = [[position[i], speed[i]] for i in range(len(position))]
        pairs.sort(reverse = True)

        stack = []

        for pair in pairs:
            p, s = pair
            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)