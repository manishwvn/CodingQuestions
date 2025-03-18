class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        start = [0, 0]
        dirs = [0, 1]

        for ins in instructions:
            if ins == "L":
                dirs = [-dirs[1], dirs[0]]
            elif ins == "R":
                dirs = [dirs[1], -dirs[0]]
            else:
                start[0] += dirs[0]
                start[1] += dirs[1]

        return start == [0, 0] or dirs != [0, 1]

        
        