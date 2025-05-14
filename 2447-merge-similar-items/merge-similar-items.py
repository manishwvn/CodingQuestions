class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:

        wt_map = {}

        for v, wt in items1:
            wt_map[v] = wt

        for v, wt in items2:
            if v in wt_map:
                wt_map[v] += wt
            else:
                wt_map[v] = wt

        res = [[v, wt] for v, wt in wt_map.items()]
        res.sort(key = lambda x: x[0])
        return res

        