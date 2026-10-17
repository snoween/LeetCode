class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0

        for ele in operations:
            if "--" in ele:
                res -= 1
            else:
                res += 1
        
        return res