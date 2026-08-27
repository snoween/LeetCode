class Twitter:

    def __init__(self):
        self.time = 0
        # Save tweet as list of tuples: (timestamp, tweetId)
        self.user_tweets = defaultdict(list)
        # Use to manage accounts following
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_tweets[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        
        # user follows themselves to get their posts
        users_to_check = self.following[userId] | {userId}
        
        for uid in users_to_check:
            for tweet in self.user_tweets[uid]:
                max_heap.append(tweet)
                
        heapq.heapify(max_heap)
        
        result = []
        while max_heap and len(result) < 10:
            _, tweetId = heapq.heappop(max_heap)
            result.append(tweetId)
            
        return result
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)