'''
# Question 1: 5 points
'''
class Quadratic:
    def __init__(self, *coef, op=None):
        self.size = len(coef)
        self.coef = list(coef)[::-1]
        self._remove_leading_zeros()
        self.op = op

    def __str__(self):
        ret_str = ''
        if self.op == '+':
            ret_str = 'The sum is'
        elif self.op == '-':
            ret_str = 'The difference is'

        for idx, val in enumerate(self.coef[::-1]):
            if idx > 0:
                ret_str += ' {SIGN}'.format(
                    SIGN='+' if val >= 0 else '-',
                )
                val = abs(val)

            if idx == self.size - 1:
                ret_str += ' {COEF}'.format(
                    COEF=val,
                )
            else:
                ret_str += ' {COEF} * x^{POWER}'.format(
                    COEF=val,
                    POWER=self.size - 1 - idx,
                )
        return ret_str

    def _remove_leading_zeros(self):
        while self.size > 1 and self.coef[-1] == 0:
            self.coef.pop()
            self.size -= 1

    def quadsum(self, q):
        new_coef = [0] * max(self.size, q.size)
        for idx, val in enumerate(self.coef):
            new_coef[idx] += val
        for idx, val in enumerate(q.coef):
            new_coef[idx] += val
        print(new_coef[::-1])
        return Quadratic(*new_coef[::-1], op='+')

    def quaddiff(self, q):
        new_coef = [0] * max(self.size, q.size)
        for idx, val in enumerate(self.coef):
            new_coef[idx] += val
        for idx, val in enumerate(q.coef):
            new_coef[idx] -= val
        return Quadratic(*new_coef[::-1], op='-')

    def is_equal(self, q):
        if self.size != q.size:
            return False
        for v, qv in zip(self.coef, q.coef):
            if v != qv:
                return False
        return True


def main():
    q1 = Quadratic(3, 8, -5)
    q2 = Quadratic(2, 3, 7)
    print(q1.quadsum(q2))
    print(q1.quaddiff(q2))
    print(q1.is_equal(q2))


if __name__ == '__main__':
    main()


'''
# Question 2: 5 points
'''
import abc


class InterestCal(object):
    def __init__(self, principal, num_years, interest_rate, num_compounds):
        """Constuctors for calculators"""
        self.principal = principal
        self.num_years = num_years
        self.interest_rate = 0.01*interest_rate
        self.num_compounds = num_compounds

    @abc.abstractmethod
    def compcal(self):
        """Computes the compound interest."""
        return

    @abc.abstractmethod
    def compout(self):
        """Prints the compounded value."""
        return


class CICal(InterestCal):
    def compcal(self):
        self.finalval = self.principal * (1 + self.interest_rate / self.num_compounds) ** (self.num_years * self.num_compounds)

    def compout(self):
        return self.finalval

class SICal(InterestCal):
    def compcal(self):
        # Notice: formula for simple interest calculation provided in problem description is wrong
        self.finalval = self.principal * (1 + self.interest_rate * self.num_years)

    def compout(self):
        return self.finalval


def main():
    c = CICal(1000,5,6,2)
    c.compcal()
    print(c.compout())

    s = SICal(1000,5,6,2)
    s.compcal()
    print(s.compout())


if __name__ == '__main__':
    main()