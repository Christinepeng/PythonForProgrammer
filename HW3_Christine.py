'''
# Question 1: 5 points
'''
class Quadratic:
    def __init__(func, *args):
        func(*args)

    def quadsum(q1, q2):
        if q1[0] + q2[0] == 0 and q1[1] + q2[1] == 0 and q1[2] + q2[2] == 0:
            print("The sum is 0")

        else:
            a = q1[0] + q2[0]
            aa = str(a)
            if a == 1:
                aa = ''

            b = q1[1] + q2[1]
            bb = '+'
            if b > 0:
                bb += str(b)
            else:
                bb = str(b)

            c = q1[2] + q2[2]
            cc = '+'
            if c > 0:
                cc += str(c)
            else:
                cc = str(c)

            print(''.join(["The sum is ", aa, "x^2", bb, "x", cc]))

    # Q1 = Quadratic(3, 8, -5)
    # Q2 = Quadratic(2, 3, 7)
    quadsum((3, 8, -5), (2, 3, 7))
    quadsum((3, 8, -5), (-3, -8, 5))

    def quaddiff(q1, q2):
        if q1[0] - q2[0] == 0 and q1[1] - q2[1] == 0 and q1[2] - q2[2] == 0:
            print("The different is 0")

        else:
            a = q1[0] - q2[0]
            aa = str(a)
            if a == 1:
                aa = ''

            b = q1[1] - q2[1]
            bb = '+'
            if b > 0:
                bb += str(b)
            else:
                bb = str(b)

            c = q1[2] - q2[2]
            cc = '+'
            if c > 0:
                cc += str(c)
            else:
                cc = str(c)

            print(''.join(["The different is ", aa, "x^2", bb, "x", cc]))

    quaddiff((3, 8, -5), (2, 3, 7))

    # def is_equal(self, q1, q2):
    #     if q1.a == q2.a and q1.b == q2.b and q1.c == q2.c:
    #         return True
    #     return False



#
# def main():
#     q = Quadratic()
#     Q1 = Quadratic(3,8,-5)
#     Q2 = Quadratic(2,3,7)
#     __init__(quadsum, Q1, Q2)
#     q.quaddiff(Q1, Q2)
#     q.is_equal(Q1, Q2)
#
#
# if __name__ == '__main__':
#     main()


'''
# Question 2: 5 points
'''
# class InterestCal:
#
#     def compound_interest_calculator(self):
#         finalval = P * ((1 + (r / n)) ^ (years * n))
#
#     def simple_interest_calculator(self):
#         finalval = P * (1 + r * n * years)
#
#     class CICal:
#         def __init__(self):
#
#
#         def compcal(self):
#
#
#         def compout(self):
#
#
#     class SICal:
#         def __init__(self):
#
#
#         def compcal(self):
#
#
#         def compout(self):
#
#
#
#
#
#
#
#
#     c = CICal(1000, 5, 6, 2)
#     c.compcal()
#     print(c.compout())
#
#     s = SICal(1000, 5, 6, 2)
#     s.compcal()
#     print(s.compout())
