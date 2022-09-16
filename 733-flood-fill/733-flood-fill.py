class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if not image or image[sr][sc] == color:
            return image
        
        m, n = len(image), len(image[0])
        dirs = [[-1,0], [0,-1], [1,0],[0,1]]
        
        src_color = image[sr][sc]
        queue = deque()
        queue.append([sr, sc])
        image[sr][sc] = color
        
        while queue:
            cr, cc = queue.popleft()
            for dir in dirs:
                nr = cr + dir[0]
                nc = cc + dir[1]

                if (nr >= 0 and nr < m) and (nc >= 0 and nc < n) and (image[nr][nc] == src_color):
                    queue.append([nr, nc])
                    image[nr][nc] = color
        return image
                
                