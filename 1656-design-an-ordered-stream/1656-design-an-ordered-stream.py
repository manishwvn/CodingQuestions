class OrderedStream:

    def __init__(self, n: int):
        self.hm = {}
        self.ptr = 1
        
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.hm[idKey] = value
        result = []
        while self.ptr in self.hm:
            result.append(self.hm[self.ptr])
            # del self.hm[self.ptr]
            self.ptr += 1
            
        return result
            
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)