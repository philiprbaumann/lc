#https://leetcode.com/problems/reorder-data-in-log-files/
class Solution(object):
    def reorderLogFiles(self, logs):
        numLogs = []
        strLogs = []
        for log in logs:
            if log.split()[1].isdigit():
                numLogs.append(log)
            else:
                strLogs.append(log)
                
        strLogs.sort(key=lambda x: x.split()[0])
        strLogs.sort(key=lambda x: x.split()[1:])
        return strLogs + numLogs     
        """
        :type logs: List[str]
        :rtype: List[str]
        """