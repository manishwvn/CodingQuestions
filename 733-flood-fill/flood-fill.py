class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if not image or image[sr][sc] == color:
            return image

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        queue = deque()
        queue.append((sr, sc))
        src = image[sr][sc]
        image[sr][sc] = color

        while queue:
            r, c = queue.popleft()

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == src:
                    queue.append((nr, nc))
                
                image[r][c] = color
        
        return image



# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
#         if not image or image[sr][sc] == color:
#             return image
        
#         dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    
#         queue = deque()
#         queue.append((sr,sc))
#         src_color = image[sr][sc]
#         image[sr][sc] = color

#         while queue:
#             r, c = queue.popleft()

#             for dr, dc in dirs:
#                 nr = r + dr
#                 nc = c + dc

#                 if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == src_color:
#                     queue.append((nr,nc))

#                 image[r][c] = color

#         return image
        

            




