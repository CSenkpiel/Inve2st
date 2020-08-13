import pandas as pd


class CalcCashflow:
    """
    This class calculates the cash flow
    """
    def __init__(self, revenue, investment, year_start_facility, opex, income, debt_share, amortization, interest):
        """
        by initialization all variables are written to the class and data frames for the results are generated
        :param revenue: revenue dataframe
        :param investment: investment dataframe
        :param year_start_facility: year in which the facility starts operation
        :param opex: opex dataframe
        :param income: income dataframe
        :param debt_share: share of debt in financing the investment
        :param amortization: amortization dataframe
        :param interest: interest dataframe
        """
        self.revenue = revenue.copy()
        self.investment = investment
        self.year_start_facility = year_start_facility
        self.opex = opex.copy()
        self.income = income.copy()
        self.debt_share = debt_share
        self.amortization = amortization
        self.interest = interest

        self.cashflow = pd.DataFrame(0, index=investment.index, columns=['project', 'financial'])
        self.income.at[self.year_start_facility - 1, 'taxes'] = 0.
        self.income = self.income.fillna(0.)
        self.opex.at[self.year_start_facility - 1, ['opex_equipment_total', 'opex_el_total']] = 0.
        self.opex = self.opex.fillna(0.)
        self.revenue[year_start_facility-1] = 0

    def calc_cashflow(self):
        """
        Calculation of cashflow from investment, revenue, opex and so on
        cashflow project = revenue - investment - opex
        cashflow financial = revenue - investment not debt - opex - financial expenses
        :return:
        """
        for i in self.cashflow.index:
            self.cashflow.at[i, 'project'] = self.revenue[i] - self.investment.at[
                i, 'capex_total'] - self.opex.at[i, 'opex_equipment_total'] - self.opex.at[i, 'opex_el_total']
            self.cashflow.at[i, 'financial'] = self.revenue[i] - self.investment.at[
                i, 'capex_total'] * (1 - self.debt_share) - self.opex.at[i, 'opex_equipment_total'] - \
                self.opex.at[i, 'opex_el_total'] - self.amortization.at[i, 'capex_total_amort'] - \
                self.interest.at[i, 'capex_total_interest'] - self.income.at[i, 'taxes']

        return self.cashflow
