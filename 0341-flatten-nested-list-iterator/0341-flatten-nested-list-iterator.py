# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]
        
    
    def next(self) -> int:
        if self.hasNext():
            nestedList, i = self.stack[-1]
            self.stack[-1][1] += 1
            return nestedList[i].getInteger()
        
    
    def hasNext(self) -> bool:
        stack = self.stack
        while stack:
            nestedList, i = stack[-1]
            if i == len(nestedList):
                stack.pop()
                
            else:
                val = nestedList[i]
                if val.isInteger(): return True
                stack[-1][1] += 1
                stack.append([val.getList(), 0])
                
        return False
                
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())