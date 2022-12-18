class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if not image or image[sr][sc] == color:
            return image
    
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r, c):
            if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == src_color:
                image[r][c] = color
                for dr, dc in dirs:
                    dfs(r+dr, c+dc)

        src_color = image[sr][sc]
        dfs(sr, sc)
        return image

                    