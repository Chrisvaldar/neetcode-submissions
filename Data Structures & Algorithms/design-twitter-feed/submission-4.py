from collections import defaultdict
class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        counter = 0
        add_back = []
        res = []
        while self.tweets and counter < 10:
            curr_user, curr_tweet = self.tweets.pop()
            if curr_user not in self.follow_map[userId] and curr_user != userId:
                add_back.append((curr_user, curr_tweet))
            else:
                res.append(curr_tweet)
                add_back.append((curr_user, curr_tweet))
                counter += 1

        while add_back:
            self.tweets.append(add_back.pop())
        print(self.tweets)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)

