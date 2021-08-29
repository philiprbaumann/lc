#https://leetcode.com/problems/time-based-key-value-store/
class TimeMap(object):

    def __init__(self):
        self.map = {}
        """
        Initialize your data structure here.
        """
        

    def set(self, key, value, timestamp):
        if key in self.map:
            self.map[key][timestamp] = value
        else:
            self.map[key] = { timestamp: value}
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        

    def get(self, key, timestamp):
        if timestamp in self.map[key]:
            return self.map[key][timestamp]
        else:
            closest, finalTime = sys.maxint, -1 
            for time in self.map[key]:
                if time < timestamp and timestamp - time < closest:
                    closest = timestamp - time
                    finalTime = time
            
            return self.map[key][finalTime] if finalTime != -1 else ""
            
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)