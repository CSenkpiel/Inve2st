import pandas as pd
import math


class CalcIncomeStatement:
    """
    This class calculates the taxes
    """
    def __init__(self, revenue, opex, interest, investment, income_tax, tech_param, technology):
        """
        by initialization all variables are written to the class and data frames for the results are generated
        :param revenue: revenue dataframe
        :param opex: opex dataframe
        :param interest: interest dataframe
        :param investment: investment dataframe
        :param income_tax: income tax rate
        :param tech_param: technical parameters dataframe
        :param technology: technology
        """
        self.revenue = revenue
        self.opex = opex
        self.interest = interest
        self.investment = investment
        self.income_tax = income_tax
        self.tech_param = tech_param
        self.technology = technology

        self.income = pd.DataFrame(index=self.opex.index)
        self.depreciation = pd.DataFrame(0., index=self.investment.index, columns=self.investment.columns)
        self.residual = pd.DataFrame(columns=investment.columns)

    def calc_ebitda(self):
        """
        Calculation of ebitda
        ebitda = revenue - opex
        in the last year the residual is added to the revenue
        :return:
        """
        self.income['ebitda'] = 0.

        for i in self.income.index:
            if i != self.income.index[-1]:
                self.income.at[i, 'ebitda'] = self.revenue[i] - self.opex.at[i, 'opex_equipment_total'] - \
                                              self.opex.at[i, 'opex_el_total']
            else:
                self.income.at[i, 'ebitda'] = self.revenue[i] + self.residual['residual_total'] -\
                                              self.opex.at[i, 'opex_equipment_total'] - \
                                              self.opex.at[i, 'opex_el_total']

    def calc_depreciation(self):
        """
        Calculation of depreciation and residual. The depreciation is the investment equally split to the lifetime of
        the component, the residual value after 25 years is stored in residual
        :return:
        """
        self.depreciation = self.depreciation.drop(columns=['capex_total'])
        self.residual = self.residual.drop(columns=['capex_total'])

        for i in self.depreciation.index:
            for j in self.depreciation.columns:
                if self.investment.at[i, j] != 0:
                    if j == 'capex_sys':
                        for k in range(i + 1, i + 1 + int(self.tech_param.at[2018, self.technology +
                                                                             '_lifetime_other_components'])):
                            self.depreciation.at[k, j] = self.investment.at[i, j] / self.tech_param.at[
                                2018, self.technology + '_lifetime_other_components']
                    elif 'recapex_sys' in j:
                        for k in range(i + 1, i + 1 + int(self.tech_param.at[2018, self.technology +
                                                                             '_lifetime_stack_y'])):
                            self.depreciation.at[k, j] = self.investment.at[i, j] / self.tech_param.at[
                                2018, self.technology + '_lifetime_stack_y']
                    elif j == 'project_capex':
                        for k in range(i + 1, i + 26):
                            self.depreciation.at[k, j] = self.investment.at[i, j] / 25
                    else:
                        a = j.split('_', 1)[-1]
                        for k in range(i + 1, i + 1 + int(self.tech_param.at[2018, a + '_lifetime'])):
                            self.depreciation.at[k, j] = self.investment.at[i, j] / self.tech_param.at[
                                2018, a + '_lifetime']

        self.depreciation = self.depreciation.fillna(0.)
        self.depreciation['depreciation_total'] = self.depreciation.sum(axis=1)
        self.income['depreciation'] = self.depreciation['depreciation_total']

        for j in self.residual.columns:
            self.residual.at[0, j] = (math.ceil(25/self.tech_param.at[2018, self.technology +
                                                                      '_lifetime_stack_y']) *
                                      self.tech_param.at[2018, self.technology + '_lifetime_stack_y'] - 25) *\
                                      self.depreciation.at[self.depreciation.index[0]+26, j]

        self.residual['residual_total'] = self.residual.sum(axis=1)

    def calc_ebit(self):
        """
        Calculation of ebit
        ebit = ebitda - depreciation
        :return:
        """
        self.income['ebit'] = self.income['ebitda'] - self.income['depreciation']

    def get_interest(self):
        """
        Store interest payments in income dataframe
        :return:
        """
        self.income['interest'] = self.interest['capex_total_interest']

    def calc_ebt(self):
        """
        Calculation of ebt
        ebt = ebit - interest
        :return:
        """
        self.income['ebt'] = self.income['ebit'] - self.income['interest']

    def calc_taxes(self):
        """
        Calculation of taxes
        taxes = ebt * tax rate
        :return:
        """
        for i in self.income.index:
            if self.income.at[i, 'ebt'] > 0:
                self.income.at[i, 'taxes'] = self.income.at[i, 'ebt'] * self.income_tax
            else:
                self.income.at[i, 'taxes'] = 0.

    def calc_income(self):
        """
        All functions are run
        :return: income data frame
        """
        self.calc_depreciation()
        self.calc_ebitda()
        self.calc_ebit()
        self.get_interest()
        self.calc_ebt()
        self.calc_taxes()

        return self.income
