class Twitter:

    def __init__(self):
        self.db = {}
        self.tweetIds = []
        self.tweets = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.db:
            self.db[userId] = {'following':[userId]}

        if not self.tweetIds:
            tid = 1
        else:    
            tid = self.tweetIds[-1] + 1
        
        self.tweetIds.append(tid)
        self.tweets[tid] = {'user': userId, 'rid': tweetId}

    def getNewsFeed(self, userId: int) -> List[int]:
        top_ten = []
        count = 0

        for tid in reversed(self.tweetIds):
            if self.tweets[tid]['user'] in self.db[userId]['following']:
                top_ten.append(self.tweets[tid]['rid'])
                count += 1
                if count == 10:
                    break

        return (top_ten)          


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.db:
            self.db[followerId] = {'following':[followerId, followeeId]}
        else:
            self.db[followerId]['following'].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        # Remove followeeId from following list of folllowerId
        if followeeId in self.db[followerId]['following']:
            self.db[followerId]['following'].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)