# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        
        def findShips(topRight, bottomLeft):
            
            if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
                return 0
            
            elif topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                return int(sea.hasShips(topRight, bottomLeft))
            
            if not sea.hasShips(topRight, bottomLeft): return 0
            
            midx = (bottomLeft.x + topRight.x) // 2
            midy = (bottomLeft.y + topRight.y) // 2
            mid = Point(midx, midy)
            
            
            q1 = findShips(Point(mid.x, topRight.y), Point(bottomLeft.x, mid.y + 1))
            q2 = findShips(topRight, Point(mid.x + 1, mid.y + 1))
            q3 = findShips(Point(topRight.x, mid.y), Point(mid.x + 1, bottomLeft.y))
            q4 = findShips(Point(mid.x, mid.y), bottomLeft)
            
            
            return q1 + q2 + q3 + q4
        
        return findShips(topRight, bottomLeft)
        