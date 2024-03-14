class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        values = self.d.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

    METHODS = {'set': set, 'get': get}


obj = TimeMap()
"""
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
"""
commands = 'set, get, get, set, get, get'
commands = commands.split(', ')
params = ('foo, bar, 1', 'foo, 1', 'foo, 3', 'foo, bar2, 4', 'foo, 4', 'foo, 5')
for com, param in zip(commands, params):
    print(TimeMap.METHODS[com](obj, *param.split(', ')))

# [null, null, "bar", "bar", null, "bar2", "bar2"]
