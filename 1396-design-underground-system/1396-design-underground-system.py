class UndergroundSystem:

    def __init__(self):
        self.idMap = dict()
        self.timeMap = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.idMap[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        tstart, startStation = self.idMap[id]

        key = (startStation, stationName)
        if key not in self.timeMap:
            self.timeMap[key] = [0, 0]

        timeInfo = self.timeMap[key]
        
        delta = t - tstart
        timeInfo[0] += 1
        timeInfo[1] += delta

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        count, t = self.timeMap[(startStation, endStation)]
        return t / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)