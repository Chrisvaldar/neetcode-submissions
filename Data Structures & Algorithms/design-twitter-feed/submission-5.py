from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.users = defaultdict(set) # userId -> {followerIDs}
        self.tweets = defaultdict(list) #userId -> [(time, tweetId)]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.users[userId].add(userId)
        for user in self.users[userId]:
            if not self.tweets[user]:
                continue
            time, tweetId = self.tweets[user][-1]
            heapEntry = (-time, tweetId, user, len(self.tweets[user]) - 1)
            heapq.heappush(heap, heapEntry)

        res = []
        
        for _ in range(10):
            if not heap:
                break
            currTime, currTweetId, currUser, currIndex = heapq.heappop(heap)
            res.append(currTweetId)
            if currIndex == 0:
                continue
            else:
                newTime, newTweetId = self.tweets[currUser][currIndex - 1]
                newEntry = (-newTime, newTweetId, currUser, currIndex - 1)
                heapq.heappush(heap, newEntry)
        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId].discard(followeeId)
