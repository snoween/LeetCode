class Solution:
    def countLargestGroup(self, n: int) -> int:
        if n < 10:
            return n

        count = 0
        nums_dict = defaultdict(int)
        
        # Make a dict = {total_digits: i}
        for i in range(1, n + 1):
            num_str = list((str(i)))
            total_digits = sum([int(x) for x in num_str])
            nums_dict[total_digits] += 1
        
        max_val = max(nums_dict.values())
        
        return list(nums_dict.values()).count(max_val)