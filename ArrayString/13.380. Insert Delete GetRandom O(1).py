# Like
# Part II, 381. Insert Delete GetRandom O(1) - Duplicates allowed
import random


class RandomizedSet(object):

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val):
        res = val not in self.dict
        if res:
            self.dict[val] = len(self.list)
            self.list.append(val)
        return res

    def remove(self, val):
        res = val in self.dict
        if res:
            idx = self.dict[val]
            lastVal = self.list[-1]
            self.list[idx] = lastVal
            self.dict[lastVal] = idx

            self.list.pop()
            del self.dict[val]
        return res

    def getRandom(self):
        return random.choice(self.list)


commands = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
values = [[], [1], [2], [2], [], [1], [2], []]

obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())  # returns 2 or 1

print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())
