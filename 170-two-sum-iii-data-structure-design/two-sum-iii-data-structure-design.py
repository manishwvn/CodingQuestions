class TwoSum:

    def __init__(self):
        self.hm = {}
        

    def add(self, number: int) -> None:
        if number in self.hm:
            self.hm[number] += 1
        else:
            self.hm[number] = 1
        

    def find(self, value: int) -> bool:
        for num in self.hm:
            if value - num == num:
                if self.hm[num] >= 2:
                    return True
            else:
                if value - num in self.hm:
                    return True

        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)