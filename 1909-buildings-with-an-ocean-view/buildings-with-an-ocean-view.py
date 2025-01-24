class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        result = [len(heights)-1]
        max_height = heights[-1]

        for i in range(len(heights)-2, -1, -1):
            curr_height = heights[i]

            if curr_height > max_height:
                result.append(i)
                max_height = curr_height
        
        print(result)
        result.reverse()
        return result
        