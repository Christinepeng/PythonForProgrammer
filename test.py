class Quadratic:
    def __init__(self, *coef):
        self.size = len(coef)
        self.coef = coef[::-1]
        self._remove_leading_zeros()

    def __str__(self):
        ret_str = 'The result is'
        for idx, val in enumerate(self.coef[::-1]):
            if idx == 0:
                ret_str += ' {COEF}x^{POWER}'.format(
                    COEF=val,
                    POWER=self.size - 1 - idx,
                )
            else:
                ret_str += ' {SIGN} {COEF}x^{POWER}'.format(
                    SIGN='+' if val >= 0 else '-',
                    COEF=abs(val),
                    POWER=self.size - 1 - idx,
                )
        return ret_str

    def _remove_leading_zeros(self):
        while self.size and self.coef[-1] == 0:
            self.coef.pop()
            self.size -= 1

    def quadsum(self, q):
        new_coef = [0] * max(self.size, q.size)
        for idx, val in enumerate(self.coef):
            new_coef[idx] += val
        for idx, val in enumerate(q.coef):
            new_coef[idx] += val
        return Quadratic(*new_coef[::-1])

    def quaddiff(self, q):
        new_coef = [0] * max(self.size, q.size)
        for idx, val in enumerate(self.coef):
            new_coef[idx] += val
        for idx, val in enumerate(q.coef):
            new_coef[idx] -= val
        return Quadratic(*new_coef[::-1])

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