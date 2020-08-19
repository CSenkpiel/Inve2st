import pandas as pd


class CalcFinancialExpenses:
    """
    class for calculation of debt expenses
    """
    def __init__(self, investment, year_start_facility, opex, debt_share, debt_term, debt_interest_rate):
        """
        by initialization all variables are written to the class and data frames for the results are generated
        :param investment: investment dateframe
        :param year_start_facility: year in which the facility starts operation
        :param opex: opex dataframe
        :param debt_share: share of debt in financing the investment
        :param debt_term: runtime of debt
        :param debt_interest_rate: interest rate for debt
        """
        self.investment = investment
        self.year_start_facility = year_start_facility
        self.opex = opex
        self.debt_share = debt_share
        self.debt_term = debt_term
        self.debt_interest_rate = debt_interest_rate

        self.new_debt = self.investment * self.debt_share
        self.amortization = pd.DataFrame(0., index=investment.index, columns=investment.columns)
        self.balance_beg = pd.DataFrame(0., index=investment.index, columns=investment.columns)
        self.balance_end = pd.DataFrame(0., index=investment.index, columns=investment.columns)
        self.interest = pd.DataFrame(0., index=investment.index, columns=investment.columns)

    def calc_financial_expenses(self):
        """
        This function calls all other functions
        :return: amortization and interest
        """
        self.calc_amortization()
        self.calc_balance()
        self.calc_interest()
        self.amortization = self.amortization.add_suffix('_amort')
        self.interest = self.interest.add_suffix('_interest')

        return self.amortization, self.interest

    def calc_amortization(self):
        """
        Calculation of the amortization
        The expenses are equally split to the runtime of debt, if the runtime exceeds the end of the project (25 years),
        the rest of the debt is payed at once
        :return:
        """
        for i in self.new_debt.index:
            for j in self.new_debt.columns:
                if self.new_debt.at[i, j] != 0.:
                    for k in range(i + 1, i + 1 + self.debt_term):
                        if k in self.new_debt.index:
                            self.amortization.at[k, j] += self.new_debt.at[i, j] / float(self.debt_term)
                        else:
                            self.amortization.at[self.new_debt.index[-1], j] += self.new_debt.at[i, j] / \
                                                                                float(self.debt_term)

        self.amortization = self.amortization.fillna(0.)

    def calc_balance(self):
        """
        Calculation of the balance of debt at the beginning and at the end of the year
        :return:
        """
        for i in self.investment.index:
            for j in self.investment.columns:
                if self.investment.at[i, j] != 0.:
                    self.balance_beg.at[i + 1, j] = self.new_debt.at[i, j]

        for k in self.balance_beg.index:
            for m in self.balance_beg.columns:
                if self.balance_beg.at[k, m] != 0.:
                    self.balance_end.at[k, m] = self.balance_beg.at[k, m] - self.amortization.at[k, m]
                    if k + 1 in self.balance_end.index:
                        self.balance_beg.at[k + 1, m] += self.balance_end.at[k, m]

        self.balance_beg = self.balance_beg.fillna(0.)
        self.balance_end = self.balance_end.fillna(0.)

    def calc_interest(self):
        """
        Calculation of the interest payment
        :return:
        """
        self.interest = self.balance_beg * self.debt_interest_rate
