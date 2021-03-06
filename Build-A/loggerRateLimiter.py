#https://leetcode.com/problems/logger-rate-limiter/
class Logger(object):

    def __init__(self):
        self.messages = {}
        """
        Initialize your data structure here.
        """
        

    def shouldPrintMessage(self, timestamp, message):
        if message in self.messages and timestamp < self.messages[message]:
            return False
        self.messages[message] = timestamp + 10
        return True 
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)