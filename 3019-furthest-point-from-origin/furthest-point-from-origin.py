class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        l, r, _ = 0, 0, 0

        for char in moves:
            if char == 'L':
                l += 1
            elif char == 'R':
                r += 1
            else:
                _ += 1
        
        return _ + abs(l - r)
        