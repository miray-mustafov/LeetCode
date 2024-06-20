# hard


class Twitter:
    fake_time = -1

    def __init__(self):
        self.followings: dict[int, set] = dict()  # dict(followerId: set[followeeIds])
        # self.tweets: dict[int, set[(int, int)]] = dict()  # dict(userId: set[tuples[tweetId,time]])
        self.tweets = []  # stack

    def postTweet(self, userId: int, tweetId: int) -> None:  # O1
        # Twitter.fake_time += 1
        # self.tweets[userId].add((tweetId, Twitter.fake_time))
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:  # On
        feed = []
        for i in range(len(self.tweets) - 1, -1, -1):
            cur_userId = self.tweets[i][0]
            if cur_userId == userId or cur_userId in self.followings.get(userId, []):
                # if user owns the tweet or followed one owns the tweet
                feed.append(self.tweets[i][1])  # cur_tweetId
            if len(feed) == 10:
                break
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:  # O1
        if not self.followings.get(followerId):
            self.followings[followerId] = set()

        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:  # O1
        if not self.followings.get(followerId) or followeeId not in self.followings[followerId]:
            return  # no such following

        self.followings[followerId].remove(followeeId)


# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[],         [1, 5],          [1],     [1, 2],    [2, 6],         [1],          [1, 2],       [1]]

user1 = 1
user2 = 2

obj = Twitter()
obj.postTweet(user1, 5)
print(obj.getNewsFeed(user1))
obj.follow(user1, user2)

obj.postTweet(user2, 6)
print(obj.getNewsFeed(user1))
obj.unfollow(user1, user2)

print(obj.getNewsFeed(user1))

from collections import defaultdict
import heapq as h


class Twitter2:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:  # O1
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:  # O
        res, minHeap = [], []

        self.followMap[userId].add(userId)  # make user follow himself for easiness
        # go greedy building a list with the last tweets of each followee
        for followeeId in self.followMap[userId]:  # Om  (m = follower's followees)
            if followeeId not in self.tweetMap:
                continue
            index = len(self.tweetMap[followeeId]) - 1
            count, tweetId = self.tweetMap[followeeId][index]
            minHeap.append((count, tweetId, followeeId, index - 1))

        h.heapify(minHeap)  # Omlogm

        while minHeap and len(res) < 10:  # O 10 logm
            count, tweetId, followeeId, index = h.heappop(minHeap)  # Ologm
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                h.heappush(minHeap, (count, tweetId, followeeId, index - 1))  # Ologm

        return res

    def follow(self, followerId: int, followeeId: int) -> None:  # O1
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:  # O1
        if followeeId in self.followMap.get(followerId, []):
            self.followMap[followerId].remove(followeeId)


user1 = 1
user2 = 2

obj2 = Twitter2()
obj2.postTweet(user1, 5)
print(obj2.getNewsFeed(user1))
obj2.follow(user1, user2)

obj2.postTweet(user2, 6)
print(obj2.getNewsFeed(user1))
obj2.unfollow(user1, user2)

print(obj2.getNewsFeed(user1))
