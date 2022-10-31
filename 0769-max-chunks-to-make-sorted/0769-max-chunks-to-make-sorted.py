class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        if len(arr) == 1:
            return 1
        
        stack = []
        count = 1
        
        for i in range(len(arr)):
            curr = arr[i]
            while stack and stack[-1] > arr[i]:
                curr = max(stack[-1], curr)
                stack.pop()
            
            stack.append(curr)
            
        return len(stack)
        