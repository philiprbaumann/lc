# https://leetcode.com/problems/design-underground-system
# Got this right off the bat.
# Need to trust my gut to use a tuple as the key instead of some nested hashes. Nested is unnecessary, although it may be quicker at scale. 
class UndergroundSystem(object):

    def __init__(self):
        self.checkTimes = defaultdict(list)
        self.times = defaultdict(list)

    def checkIn(self, id, stationName, t):
        self.checkTimes[id] = [stationName, t]
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        

    def checkOut(self, id, stationName, t):
        stationStart, tStart = self.checkTimes.pop(id)
        self.times[(stationStart, stationName)].append(t-tStart)
        
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        

    def getAverageTime(self, startStation, endStation):
        return float(sum(self.times[(startStation, endStation)])) / len(self.times[(startStation,endStation)])
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)