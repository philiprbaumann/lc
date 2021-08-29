#https://leetcode.com/problems/optimal-account-balancing/
class Solution(object):
    def minTransfers(self, transactions):
        counter = collections.Counter()
        for f, t, m in transactions:
            counter[f] -= m
            counter[t] += m
        balances = counter.values()
        def dfs(b):
            if not b:
                return 0
            if not b[0]:
                return dfs(b[1:])
            for i in range(1, len(b)):
                if b[i] == -b[0]:
                    return 1 + dfs(b[1:i] + [0] + b[i+1:])
            ret = []
            for i in range(1, len(b)):
                if b[i] * b[0] < 0:
                    ret.append(dfs(b[1:i] + [b[i]+b[0]] + b[i+1:]))
            return 1+min(ret)

        return dfs(balances)