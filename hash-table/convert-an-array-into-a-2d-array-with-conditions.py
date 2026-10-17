class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums_dict = {}
        max_count = 0

        # Make a dict = {num: occurrence times}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 0
            nums_dict[num] += 1
            max_count = max(max_count, nums_dict[num])     # Get the highgest occurrence times

        result = [[] for _ in range(max_count)]
        
        for num, count in nums_dict.items():
            for i in range(max_count):
                result[i].append(num)
                count -= 1
                
                if count == 0:
                    break
        
        return result