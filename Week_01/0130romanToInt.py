class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        nums = 0
        length = len(s)
        if length == 1:
            return roman[s]
        for i in range(len(s)):
            if i < length - 1 and roman[s[i]] < roman[s[i + 1]]:
                nums -= roman[s[i]]
            else:
                nums += roman[s[i]]
        return nums
