class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food = {}
        self.cuisine = defaultdict(list)
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food[food] = (rating, cuisine)
            heapq.heappush(self.cuisine[cuisine], (-rating, food))


    def changeRating(self, food: str, newRating: int) -> None:
        _, cuisine = self.food[food]
        self.food[food] = (newRating, cuisine)

        heapq.heappush(self.cuisine[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine[cuisine]

        while heap:
            negativeRating, food = heap[0]
            currentRating, _ = self.food[food]

            if -negativeRating == currentRating:
                return food
            
            heapq.heappop(heap)

        return ""

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)