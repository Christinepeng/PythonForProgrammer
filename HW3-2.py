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