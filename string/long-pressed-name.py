class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0

        for char in typed:
            if i < len(name) and name[i] == char:
                i += 1
        
        return i == len(name)