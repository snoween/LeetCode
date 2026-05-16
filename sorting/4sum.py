class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        seen_a, seen_res = set(), set()
        result = []

        for i in range(len(nums)):
            if nums[i] in seen_a:
                continue
            seen_a.add(nums[i])
            num_a = nums[i]

            seen_b = set()
            for j in range(i+1, len(nums)):
                if nums[j] in seen_b:
                    continue

                seen_b.add(nums[j])
                num_b = nums[j]

                c = j + 1
                d = len(nums) - 1

                while c < d:
                    if num_a + num_b + nums[c] + nums[d] < target:
                        c += 1
                    
                    elif num_a + num_b + nums[c] + nums[d] > target:
                        d -= 1
                    
                    else:
                        if tuple([num_a, num_b, nums[c], nums[d]]) not in seen_res:
                            result.append([num_a, num_b, nums[c], nums[d]])
                            seen_res.add(tuple([num_a, num_b, nums[c], nums[d]]))
                        
                        c += 1
                        d -= 1
        
        return result
