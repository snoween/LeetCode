class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        # func to get all posible arrays (start index, path)
        def find_path(start_index, path):
            # if len path >= 2 -> valid -> append COPY path to result
            if len(path) >= 2:
                result.append(path[:])
            # create seen set to avoid append same path -> add num (starting point)
            seen = set()
            # loop through len nums from start index -> end
            for i in range(start_index, len(nums)):
                # if num in seen -> path exists -> continue 
                if nums[i] in seen:
                    continue
                # if no path of num >= last num in path
                if not path or nums[i] >= path[-1]:
                    # seen add num
                    seen.add(nums[i])
                    # path append num 
                    path.append(nums[i])
                    # recursion: func (start index = i, path = path)
                    find_path(start_index = i + 1, path = path)
                    # pop path
                    path.pop()
        
        # func (start index = 0, path = [])
        find_path(start_index = 0, path = [])
        # return result
        return result
                    