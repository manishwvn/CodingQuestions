class Twitter:

    def __init__(self):
        
        self.count = 0
        self.tweets = {}
        self.followers = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
            
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        
        heap = []
        
        if userId in self.tweets:
            for tweet in self.tweets[userId]:
                heappush(heap, tweet)
                
        if userId in self.followers:
            for followee in self.followers[userId]:
                if followee in self.tweets:
                    for tweet in self.tweets[followee]:
                        heappush(heap, tweet)
                        
        result = []
        while heap and len(result) < 10:
            result.append(heappop(heap)[1])
            
        return result
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()            
        self.followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)