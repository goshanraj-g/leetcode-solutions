class Solution(object):
    def fizzBuzz(self, n):
        array = []
        fizz = 3
        buzz = 5
        while n > 0:
            if n % fizz == 0 and n % buzz == 0:
                array.append("FizzBuzz")
            elif n % fizz == 0:
                array.append("Fizz")
            elif n % buzz == 0:
                array.append("Buzz")
            else:
                array.append(str(n))
            n -= 1
        return array[::-1]
