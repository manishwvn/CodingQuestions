class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dis= 10000 
        ind = -1
        for i in range (len (points)):
            if points[i][0] == x or points [i][1] == y:
                mandist = abs(points[i][0] -x) + abs(points[i][1] - y)
                if mandist < min_dis :
                    min_dis = mandist
                    ind = i
        return ind