class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        x = y = i = 0
        
        for inst in instructions:
            if inst == 'G':
                x += dirs[i][0]
                y += dirs[i][1]
                
            elif inst == 'L':
                i = (i + 3) % 4
                
            else:
                i = (i + 1) % 4
                
        return (x == 0 and y == 0) or i != 0
        