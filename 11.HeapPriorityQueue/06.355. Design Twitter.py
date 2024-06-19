# hard

class Twitter:
    fake_time = -1

    def __init__(self):
        self.followings: dict[int, set] = dict()  # dict(followerId: set[followeeIds])
        # self.tweets: dict[int, set[(int, int)]] = dict()  # dict(userId: set[tuples[tweetId,time]])
        self.tweets = []  # stack

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Twitter.fake_time += 1
        # self.tweets[userId].add((tweetId, Twitter.fake_time))
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        feed = []
        for i in range(len(self.tweets) - 1, -1, -1):
            cur_userId = self.tweets[i][0]
            if cur_userId == userId or cur_userId in self.followings.get(userId, []):
                # if user owns the tweet or followed one owns the tweet
                feed.append(self.tweets[i][1])  # cur_tweetId
            if len(feed) == 10:
                break
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.followings.get(followerId):
            self.followings[followerId] = set()

        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
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



# operations = {
#     'Twitter': Twitter,
#     'postTweet': self.postTweet,
#     'getNewsFeed': Twitter,
#     'follow': Twitter,
#     'unfollow': Twitter,
# }
