class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0

        for j, char in enumerate(typed):
            if i < len(name) and name[i] == char:
                i += 1
            elif i > 0 and name[i-1] == char:
                continue
            else:
                return False
            
        return i == len(name)