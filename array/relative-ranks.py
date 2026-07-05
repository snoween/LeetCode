class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_negative = [-num for num in score]
        heapq.heapify(score_negative)
        
        rewards = defaultdict()
        
        for i in range(len(score)):
            if i == 0:
                rewards[heapq.heappop(score_negative)] = "Gold Medal"                  
            elif i == 1:
                rewards[heapq.heappop(score_negative)] = "Silver Medal"
            elif i == 2:
                rewards[heapq.heappop(score_negative)] = "Bronze Medal"
            else:
                rewards[heapq.heappop(score_negative)] = str(i + 1)
        
        result = []
        for num in score:
            result.append(rewards[-num])
        
        return result