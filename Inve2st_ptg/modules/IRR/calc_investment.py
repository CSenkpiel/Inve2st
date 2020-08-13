import pandas as pd
import math


class CalcInvestment:
    """
    Class to calculate the investment costs
    """
    def __init__(self, year_start_facility, sector, technology, size, trend, investment_sys, tech_param,
                 investment_other):
        """
        by initialization all relevant data is written to the class and an investment data frame is generated
        :param year_start_facility: year in which the facility starts operation
        :param sector: sector
        :param technology: electrolysis technology
        :param size: size of facility
        :param trend: optimistic or pessimistic
        :param investment_sys: investment costs for the system
        :param tech_param: technical parameters
        :param investment_other: other investment costs
        """
        self.year_start_facility = year_start_facility
        self.sector = sector
        self.technology = technology
        self.size = size
        self.trend = trend
        self.investment_sys = investment_sys
        self.tech_param = tech_param
        self.investment_other = investment_other

        self.investment = pd.DataFrame(index=range(self.year_start_facility - 1, self.year_start_facility+25))

    def calc_invest(self):
        """
        Runs all of the functions and stores the sum in the investment data frame
        :return: investment data frame
        """
        self.calc_electrolysis_invest()
        self.calc_project_capex()
        self.calc_compressor_invest()
        self.calc_storage_tank_invest()
        self.calc_salt_cavern_invest()
        self.calc_filling_center_invest()
        self.calc_trailer_invest()
        self.calc_truck_invest()
        self.calc_hrs_invest()
        self.calc_injection_station_invest()
        self.calc_gas_turbine_invest()

        self.investment = self.investment.astype(float)
        self.investment['capex_total'] = self.investment.sum(axis=1)
        return self.investment

    def calc_electrolysis_invest(self):
        """
        Calculation of the start investment and replacement investments of the electrolysis system
        at the beginning:
        capex = price [Euro/kWel] * size (MWel) * 1000
        replacement:
        capex = price [Euro/kWel] * size (MWel) * 1000 * 0.5
        :return:
        """
        self.investment['capex_sys'] = 0
        start = self.year_start_facility
        technology = self.technology
        size = str(self.size)
        trend = self.trend

        self.investment.at[start - 1, 'capex_sys'] = self.investment_sys.at[start - 1, technology + "_" + size + "_" +
                                                                            trend] * self.size * 1000
        lifetime = int(self.tech_param.at[2018, technology + "_lifetime_stack_y"])
        replace = math.floor(25 / lifetime)

        for i in range(replace):
            year = start - 1 + (i + 1) * lifetime
            self.investment['recapex_sys_' + str(i)] = 0
            self.investment.at[year, 'recapex_sys_' + str(i)] = self.investment_sys.at[year, technology + "_" + size +
                                                                                       "_" + trend] * \
                self.size * 1000 * 0.5

    def calc_project_capex(self):
        """
        Calculation of the project capex, based on Hinicio (2017)
        project_capex = capex_sys * factor
        :return:
        """
        self.investment['project_capex'] = self.investment['capex_sys'] * (0.1 * (2.5 / self.size) + 0.35)

    def calc_compressor_invest(self):
        """
        Calculation of the investment for a compressor. A compressor is needed if the pressure of the system smaller
        than the pressure of the storage tank.
        The value was calculated in an excel sheet and depends on the ratio of the pressures and the produced amount of
        hydrogen. It bases on Hinicio (2017)
        Maybe the formula will be implemented here one day
        :return:
        """
        self.investment['capex_compressor'] = 0
        tech = self.tech_param
        if self.size == 3.1 and self.sector in ['mobility', 'industry'] and \
                tech.at[self.year_start_facility, self.technology + "_pressure"] < \
                tech.at[self.year_start_facility, "storage_tank_pressure"]:
            self.investment.at[self.year_start_facility - 1, 'capex_compressor'] = 108111
        elif self.size == 10 and self.sector in ['mobility', 'industry'] and \
                tech.at[self.year_start_facility, self.technology + "_pressure"] < \
                tech.at[self.year_start_facility, "storage_tank_pressure"]:
            self.investment.at[self.year_start_facility - 1, 'capex_compressor'] = 234192

    def calc_storage_tank_invest(self):
        """
        Calculation of the start investment for the storage tank.
        capex_storage_tank = factor [Euro/kg] * storage_tank_size
        :return:
        """
        self.investment['capex_storage_tank'] = 0

        if self.size == 3.1 and self.sector in ['mobility', 'industry']:
            size = 'storage_tank_size_1'
            size_tank = self.tech_param.at[2018, size]
            factor = 600
        elif self.size == 10 and self.sector in ['mobility', 'industry']:
            size = 'storage_tank_size_2'
            size_tank = self.tech_param.at[2018, size]
            factor = 500
        else:
            size_tank = 0
            factor = 0

        self.investment.at[self.year_start_facility - 1, 'capex_storage_tank'] = size_tank * factor

    def calc_salt_cavern_invest(self):
        """
        Calculation of the start investment for a salt cavern based on Reuß (2017) and Planet (2014)
        capex_salt_cavern = factor * (size/500000)^0.28
        :return:
        """
        self.investment['capex_salt_cavern'] = 0

        if self.size == 310:
            size = 'salt_cavern_size_1'
            size_cavern = self.tech_param.at[2018, size]
        elif self.size == 590:
            size = 'salt_cavern_size_2'
            size_cavern = self.tech_param.at[2018, size]
        elif self.size == 1000:
            size = 'salt_cavern_size_3'
            size_cavern = self.tech_param.at[2018, size]
        else:
            size_cavern = 0

        factor = 92600000
        self.investment.at[self.year_start_facility - 1, 'capex_salt_cavern'] = factor * (size_cavern / 500000) ** 0.28

    def calc_filling_center_invest(self):
        """
        Calculation of the start investment for a filling center based on Hinicio (2017)
        Was calculated in Excel. Could be implemented someday
        :return:
        """
        self.investment['capex_filling_center'] = 0
        if self.size == 10 and self.sector in ['mobility', 'industry'] and self.year_start_facility < 2031:
            capex_filling_center = 1607350
        elif self.size == 10 and self.sector in ['mobility', 'industry'] and self.year_start_facility >= 2031:
            capex_filling_center = 1507122
        else:
            capex_filling_center = 0
        self.investment.at[self.year_start_facility - 1, 'capex_filling_center'] = capex_filling_center

    def calc_trailer_invest(self):
        """
        Calculation of the start investment and replacement investments for a trailer. The price depends on the size of
        the trailer and is assumed to be constant over years
        :return:
        """
        self.investment['capex_trailer'] = 0
        start = self.year_start_facility
        trailer_exists = False

        if self.size == 10 and self.sector in ['mobility', 'industry']:
            self.investment.at[start - 1, 'capex_trailer'] = 2100 * self.tech_param.at[start - 1, "trailer_size"]
            trailer_exists = True

        if trailer_exists:
            lifetime = int(self.tech_param.at[2018, "trailer_lifetime"])
            replace = math.floor(25 / lifetime)

            for i in range(replace):
                year = start - 1 + (i + 1) * lifetime
                self.investment.at[year, 'capex_trailer'] = self.investment.at[start - 1, 'capex_trailer']

    def calc_truck_invest(self):
        """
        Calculation of the start investment and replacement investments for a truck, the price is constant over years
        :return:
        """
        self.investment['capex_truck'] = 0
        start = self.year_start_facility
        truck_exists = False

        if self.size == 10 and self.sector in ['mobility', 'industry']:
            self.investment.at[start - 1, 'capex_truck'] = 480000
            truck_exists = True

        if truck_exists:
            lifetime = int(self.tech_param.at[2018, "truck_lifetime"])
            replace = math.floor(25 / lifetime)

            for i in range(replace):
                year = start - 1 + (i + 1) * lifetime
                self.investment.at[year, 'capex_truck'] = self.investment.at[start - 1, 'capex_truck']

    def calc_hrs_invest(self):
        """
        Read in the start investment for a hydrogen refueling station
        :return:
        """
        self.investment['capex_hrs'] = 0
        start = self.year_start_facility
        if self.sector == 'mobility':
            self.investment.at[start - 1, 'capex_hrs'] = self.investment_other.at[start - 1, 'HRS_' + str(self.size)]

    def calc_injection_station_invest(self):
        """
        Calculation of the start investment for a injection station
        :return: investment data frame
        """
        self.investment['capex_injection_station'] = 0
        start = self.year_start_facility

        if self.size > 10 and self.sector == 'injection':
            self.investment.at[start - 1, 'capex_injection_station'] = self.investment_other.at[
                start - 1, 'injection_station_transmission']
        elif self.size <= 10 and self.sector == 'injection':
            self.investment.at[start - 1, 'capex_injection_station'] = self.investment_other.at[
                start - 1, 'injection_station_distribution']

    def calc_gas_turbine_invest(self):
        """
        Read in the start investment for a gas turbine, only values for size = 310 available,
        adjust to further data
        :return: investment data frame
        """
        self.investment['capex_gas_turbine'] = 0
        start = self.year_start_facility

        if self.sector == 're_electrification' and self.size == 310:
            self.investment.at[start - 1, 'capex_gas_turbine'] = self.investment_other.at[
                start - 1, 'gas_turbine_' + str(self.size)]
