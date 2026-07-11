class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # nums = [1,1,2,2,3,4,2,3], k = 6, x = 2
        # first loop:
        # curr_freq[0:6] = {1: 2, 2: 2, 3: 1, 4: 1}
        # x = 2 -> take 1 * 2 + 2 * 2 = 6
        # second loop:
        # curr_freq[1:7] = {1: 1, 2: 3, 3: 1, 4: 1}
        # x = 2 -> take 2 * 3 + 4 * 1 = 10 - equal freq -> choose max

        # Use sliding window to update curr_freq - fixed size
        # heap for freq?

        freq = defaultdict(lambda: 0)
        output = []
        total = 0
        # set up init curr_freq
        for i in range(k):
            freq[nums[i]] += 1
        
        def getMinFreq(freq, x):
            freq_val = list(freq.values())
            heapq.heapify(freq_val)
            total = 0

            while len(freq_val) > x:
                heapq.heappop(freq_val)
            
            valid_num = []
            heapq.heapify(valid_num)
            for num in freq:
                if freq[num] in set(freq_val):
                    heapq.heappush(valid_num, num)
            
            return valid_num
        
        def calculateSum(freq, x):
            top = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))[:x]
            return sum(num * cnt for num, cnt in top)
                
        output.append(calculateSum(freq, x))
        left = 0

        for right in range(k, len(nums)):
            freq[nums[right]] += 1
            freq[nums[left]] -= 1
            
            if freq[nums[left]] == 0:
                del freq[nums[left]]

            left += 1
            output.append(calculateSum(freq, x))
            
        return output
