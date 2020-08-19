import pandas as pd


class PTGData:
    """
    This class reads in all data and calculates the hydrogen production, efficiency, full load hours, electric
    consumption and revenues
    """
    def __init__(self, path_hist, path_sale, path_investment_sys, path_investment_other, path_tech, path_opex,
                 path_purchase, path_pol):
        """
        All csv files from the inputs folder are read in when initializing, the parameters are the paths.
        In addition the DataFrames for the calculations are created
        :param path_hist:
        :param path_sale:
        :param path_investment_sys:
        :param path_investment_other:
        :param path_tech:
        :param path_opex:
        :param path_purchase:
        :param path_pol:
        """
        self.hist = pd.read_csv(path_hist, sep=";", comment="#", index_col=0)
        self.sale_prices = pd.read_csv(path_sale, sep=";", comment="#", index_col=0)
        self.investment_sys = pd.read_csv(path_investment_sys, sep=";", comment="#", index_col=0)
        self.investment_other = pd.read_csv(path_investment_other, sep=";", comment="#", index_col=0)
        self.tech_param = pd.read_csv(path_tech, sep=";", comment="#", index_col=0)
        self.opex = pd.read_csv(path_opex, sep=";", comment="#", index_col=0)
        self.purchase_prices = pd.read_csv(path_purchase, sep=";", comment="#", index_col=0)
        self.pol = pd.read_csv(path_pol, sep=";", comment="#", index_col=0)

        self.hydrogen_production = pd.DataFrame(index=range(2019, 2081))
        self.efficiency = pd.DataFrame(index=range(2019, 2081))
        self.full_load_hours = pd.DataFrame(index=range(2019, 2081))
        self.electric_consumption = pd.DataFrame(index=range(2019, 2081))
        self.revenue = pd.DataFrame(index=range(2019, 2081))

        self.calculate_data()

    def calculate_data(self):
        """
        Here all calculations are started
        :return:
        """
        self.calc_hydrogen_production()
        self.calc_efficiency()
        self.calc_full_load_hours()
        self.calc_electric_consumption()
        self.calc_revenue()

    def calc_hydrogen_production(self):
        """
        Calculation of annual production of hydrogen in kg. At the moment constant, can be adjusted in future
        :return:
        """
        self.hydrogen_production['annual_hydrogen_production_3.1'] = 339450
        self.hydrogen_production['annual_hydrogen_production_10'] = 1095000
        self.hydrogen_production['annual_hydrogen_production_310'] = 14267627
        self.hydrogen_production['annual_hydrogen_production_590'] = 67000000

    def calc_efficiency(self):
        """
        Calculation of efficiency for AEL and PEM technology
        :return:
        """
        for i in self.efficiency.index:
            if i < 2050:
                j = i - 2018
                self.efficiency.at[i, 'AEL_optimistic'] = 0.0016 * j + 0.6484
                self.efficiency.at[i, 'AEL_pessimistic'] = 0.0016 * j + 0.5984
                self.efficiency.at[i, 'PEM_optimistic'] = 0.0032 * j + 0.5968
                self.efficiency.at[i, 'PEM_pessimistic'] = 0.0032 * j + 0.5468

            else:
                self.efficiency.at[i, 'AEL_optimistic'] = 0.7
                self.efficiency.at[i, 'AEL_pessimistic'] = 0.65
                self.efficiency.at[i, 'PEM_optimistic'] = 0.7
                self.efficiency.at[i, 'PEM_pessimistic'] = 0.65

    def calc_full_load_hours(self):
        """
        Calculation of full load hours, depends on technology, size, efficiency and hydrogen production.
        full load hours = hydrogen production [MWh] / (size * efficiency)
        conversion factor (LHV) = 33.33 [kWh/kg]
        :return:
        """
        for technology in ['AEL', 'PEM']:
            for size in [3.1, 10, 310, 590]:
                for trend in ['optimistic', 'pessimistic']:
                    for i in self.full_load_hours.index:
                        self.full_load_hours.at[i, 'flh_' + technology + '_' + str(size) + '_' + trend] = \
                            (self.hydrogen_production.at[2019, 'annual_hydrogen_production_' + str(size)] * 33.33 /
                             1000) / (self.efficiency.at[i, technology + '_' + trend] * size)

    def calc_electric_consumption(self):
        """
        Calculation of electric consumption, depends on technology, size and full load hours.
        electric consumption = full load hours * size = hydrogen production [MWh] / efficiency
        :return:
        """
        for technology in ['AEL', 'PEM']:
            for size in [3.1, 10, 310, 590]:
                for trend in ['optimistic', 'pessimistic']:
                    for i in self.electric_consumption.index:
                        self.electric_consumption.at[i, 'electric_consumption_' + technology + '_' + str(size) + '_'
                                                     + trend] = self.full_load_hours.at[i, 'flh_' + technology + '_'
                                                                                        + str(size) + '_' + trend] * \
                            size

    def calc_revenue(self):
        """
        Calculation of the revenue depends on sector, size, hydrogen production and sales prices
        revenue = hydrogen production [kg or MWh] * sale price [ct/kWh or Euro/kg]
        :return:
        """
        sector = 'mobility'
        for size in [3.1, 10]:
            for trend in ['optimistic', 'pessimistic']:
                for i in self.revenue.index:
                    self.revenue.at[i, 'revenue_' + sector + '_' + str(size) + '_' + trend] = \
                       self.hydrogen_production.at[i, 'annual_hydrogen_production_' + str(size)] * \
                       float(self.sale_prices.at[i, sector + "_" + trend])

        sector = 'industry'
        for size in [3.1, 10]:
            for trend in ['optimistic', 'pessimistic']:
                for i in self.revenue.index:
                    self.revenue.at[i, 'revenue_' + sector + '_' + str(size) + '_' + trend] = \
                         self.hydrogen_production.at[i, 'annual_hydrogen_production_' + str(size)] * \
                         float(self.sale_prices.at[i, sector + '_' + str(size) + "_" + trend])

        sector = 'injection'
        # change unit from kg to kWh and divide by 100 to convert to Euro because sales price is in cent/kWh also for
        # re_electrification
        hydrogen_production = self.hydrogen_production * 33.33 / 100
        for size in [10, 590]:
            for trend in ['optimistic', 'pessimistic']:
                for i in self.revenue.index:
                    self.revenue.at[i, 'revenue_' + sector + '_' + str(size) + '_' + trend] = \
                        hydrogen_production.at[i, 'annual_hydrogen_production_' + str(size)] * \
                        float(self.sale_prices.at[i, sector + "_" + trend])

        sector = 're_electrification'
        for size in [10, 310, 590]:
            for trend in ['optimistic', 'pessimistic']:
                for i in self.revenue.index:
                    self.revenue.at[i, 'revenue_' + sector + '_' + str(size) + '_' + trend] = \
                        hydrogen_production.at[i, 'annual_hydrogen_production_' + str(size)] * \
                        float(self.sale_prices.at[i, "electricity_" + trend])
