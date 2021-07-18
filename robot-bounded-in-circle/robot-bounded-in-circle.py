class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        dirs = [[0,1], [1,0], [0,-1],[-1,0]]
        
        x, y = 0, 0
        
        idx = 0
        
        for ins in instructions:
            if ins == 'L':
                idx = (idx + 3) % 4
                
            elif ins == 'R':
                idx = (idx + 1) % 4
                
            else:
                x += dirs[idx][0]
                y += dirs[idx][1]
                
        return (x == 0 and y == 0) or idx != 0
                
        