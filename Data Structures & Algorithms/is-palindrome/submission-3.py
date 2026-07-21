class Solution:
    def isPalindrome(self, s: str) -> bool:
        first_half = len(s) // 2
        second_half = len(s) - first_half
        count1 = 0
        count2 = len(s) - 1
        while count1 < count2:
            while not s[count1].isalnum() and count1 < count2:
                count1 += 1
            while not s[count2].isalnum() and count2 > count1:
                count2 -= 1
            if s[count1].lower() != s[count2].lower():
                return False
            count1 += 1
            count2 -= 1
        return True



