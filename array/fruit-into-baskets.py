class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        typeFruits = defaultdict(int)
        maxFruits = 0

        left = 0
        for right, num in enumerate(fruits):
            typeFruits[num] += 1
            
            while len(typeFruits) > 2:
                typeFruits[fruits[left]] -= 1
                if typeFruits[fruits[left]] == 0:
                    del typeFruits[fruits[left]]
                left += 1
            
            maxFruits = max(maxFruits, right - left + 1)
        
        return maxFruits      