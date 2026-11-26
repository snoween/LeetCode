class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters)

        while left < right:
            middle = left + (right - left) // 2
            if letters[middle] > target:
                right = middle
            else:
                left = middle + 1
        
        return letters[left] if left < len(letters) else letters[0]