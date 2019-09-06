'''
Question 1: 5points

Modified version of problem #414 from project Euler
(https://projecteuler.net/problem=414)


6174 is a remarkable number; if we sort its digits in increasing order
and subtract that number from the number you get when you sort the digits
in decreasing order, we get 7641-1467=6174. Even more remarkable is that
if we start from any 4 digit number and repeat this process of sorting and
subtracting, we'll eventually end up with 6174 or immediately with 0 if
all digits are equal. This also works with numbers that have less than 4
digits if we pad the number with leading zeroes until we have 4 digits.
E.g. let's start with the number 0837:
8730-0378=8352
8532-2358=6174

6174 is called the Kaprekar constant. The process of sorting and
subtracting and repeating this until either 0 or the Kaprekar constant
is reached is called the Kaprekar routine.

Write a Python program to calculate the number of steps to reach the
Kaprekar constant for values 8730 and 9730.
'''
class Solution:
    def stepsToKaprekarConstant(self, num):
        cnt = 0
        while num != 6174 and num != 0:
            lst = [i for i in str(num)]
            min_num = sorted(lst)
            max_num = min_num[::-1]
            num = int(''.join(max_num)) - int(''.join(min_num))
            cnt += 1
        return (cnt)


sol = Solution()
test_cases = [8730, 9730]
for test_case in test_cases:
    print(sol.stepsToKaprekarConstant(test_case))


'''
Question 2: 5 points

https://en.wikipedia.org/wiki/Run-length_encoding

Implement an encoding scheme.

A string 
WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW 
has 67 characters. Write a Python program to convert this string to 
12W1B12W3B24W1B14W. The new string is created
by calculating the number of times a characters appears consecutively and
placing the character next to it. The new string only needs 18 character,
thus compressing the original string by 73%.
'''
class Solution:
    def charactersCalculate(self, s):
        if len(s) == 0:
            return ''
        else:
            cnt = 0
            tgt = s[0]
            res = []
            for c in s:
                if c != tgt:
                    res.extend([str(cnt), tgt])
                    tgt = c
                    cnt = 1
                else:
                    cnt += 1
            res.extend([str(cnt), tgt])
            return ''.join(res)

sol = Solution()
print(sol.charactersCalculate('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'))