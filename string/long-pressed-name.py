class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        count = 0

        for j, char in enumerate(typed):
            if i < len(name) and name[i] == char:
                i += 1
                count += 1
            print(i, j)
            if i == len(name) and char != name[i-1]:
                return False

        return count == len(name)