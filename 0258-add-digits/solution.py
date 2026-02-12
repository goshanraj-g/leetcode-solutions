class Solution(object):
    def addDigits(self, num):
        res = num
        while res >= 10:
            strNum = str(res)
            current_sum = 0
            for n in strNum:
                current_sum += int(n)
            res = current_sum
        return res
