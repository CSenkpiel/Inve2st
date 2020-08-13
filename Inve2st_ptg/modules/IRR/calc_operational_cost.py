import pandas as pd


class CalcOperationalCost:
    """
    This class calculates the operational costs
    """
    def __init__(self, investment, sector, year_start_facility, technology, size, el_source, trend, buy_price,
                 opex, purchase_prices):
        """
        by initializing the variables are written to the class and data frames for opex are generated
        :param investment: dataframe with investment costs
        :param year_start_facility: year in which the facility starts operation
        :param technology: AEL or PEM
        :param size: size of facility
        :param opex: opex factors
        :param purchase_prices: energy purchase prices
        """
        self.investment = investment
        self.sector = sector
        self.year_start_facility = year_start_facility
        self.technology = technology
        self.size = size
        self.el_source = el_source
        self.trend = trend
        self.buy_price = buy_price
        self.opex = opex
        self.purchase_prices = purchase_prices

        self.opex_data = pd.DataFrame(index=investment.index)
        self.opex_data = self.opex_data.drop(index=(self.year_start_facility-1))

    def calc_equipment_opex(self):
        """
        Calculation of operational costs for equipment
        opex = investment * opex factor
        :return:
        """
        self.opex_data['opex_sys'] = self.investment.at[self.year_start_facility - 1, 'capex_sys'] * \
            self.opex.at[1, self.technology]
        self.opex_data['opex_compressor'] = self.investment.at[self.year_start_facility - 1, 'capex_compressor'] * \
            self.opex.at[1, 'compressor']
        self.opex_data['opex_storage_tank'] = self.investment.at[self.year_start_facility - 1, 'capex_storage_tank'] * \
            self.opex.at[1, 'storage_tank']
        self.opex_data['opex_salt_cavern'] = self.investment.at[self.year_start_facility - 1, 'capex_salt_cavern'] * \
            self.opex.at[1, 'salt_cavern']
        self.opex_data['opex_filling_center'] = self.investment.at[self.year_start_facility - 1,
                                                                   'capex_filling_center'] * \
            self.opex.at[1, 'filling_center']
        self.opex_data['opex_trailer'] = self.investment.at[self.year_start_facility - 1, 'capex_trailer'] * \
            self.opex.at[1, 'trailer']
        self.opex_data['opex_truck'] = self.investment.at[self.year_start_facility - 1, 'capex_truck'] * \
            self.opex.at[1, 'truck']
        self.opex_data['opex_hrs'] = self.investment.at[self.year_start_facility - 1, 'capex_hrs'] * \
            self.opex.at[1, 'HRS']
        self.opex_data['opex_injection_station'] = self.investment.at[self.year_start_facility - 1,
                                                                      'capex_injection_station'] * \
            self.opex.at[1, 'injection_station']
        self.opex_data['opex_gas_turbine'] = self.investment.at[self.year_start_facility - 1, 'capex_gas_turbine'] * \
            self.opex.at[1, 'gas_turbine']
        self.opex_data['opex_equipment_total'] = self.opex_data.sum(axis=1)

    def calc_electricity_opex(self, flh, electric_consumption):
        """
        Calculation of operational costs for electricity, factor 10 is to convert from ct per kWh to Euro per MWh
        electric cost = electric consumption * price
        at 1 GW the price changes, for self-consumption above 3100 full load hours a surcharge is to pay
        :return:
        """
        self.opex_data['el_cost_over_1000'] = 0
        self.opex_data['el_cost_under_1000'] = 0
        self.opex_data['surcharge_3100_flh'] = 0

        if self.sector == 're_electrification':
            if self.el_source == 'self-consumption':
                for i in self.opex_data.index:
                    self.opex_data.at[i, 'el_cost_under_1000'] = float(self.purchase_prices.at[i, self.el_source +
                                                                                               "_under_1000MWh_" +
                                                                                               self.trend]) * \
                                                                 min(1000, electric_consumption.at[
                                                                     i, 'electric_consumption_' + self.technology +
                                                                     '_' + str(self.size) + '_' + self.trend]) * 10

                    self.opex_data.at[i, 'el_cost_over_1000'] = float(self.purchase_prices.at[i, self.el_source +
                                                                                              '_' +
                                                                                              self.buy_price +
                                                                                              "_over_1000MWh_" +
                                                                                              self.trend]) * \
                        max(0, electric_consumption.at[i, 'electric_consumption_' + self.technology + '_' +
                                                       str(self.size) + '_' + self.trend] - 1000) * 10

                    if flh.at[i, 'flh_' + self.technology + '_' + str(self.size) + '_' + self.trend] > 3100:
                        d = float(self.purchase_prices.at[i, "grid_full_over_1000MWh_" + self.trend]) - \
                            float(self.purchase_prices.at[i, "self-consumption_energy_intensive_over_1000MWh_" +
                                  self.trend])
                        self.opex_data.at[i, 'surcharge_3100_flh'] = d * 10 * self.size * \
                            max(0, flh.at[i, 'flh_' + self.technology + '_' + str(self.size) + '_' + self.trend] - 3100)
            else:
                for i in self.opex_data.index:
                    self.opex_data.at[i, 'el_cost_under_1000'] = float(self.purchase_prices.at[i, self.sector +
                                                                                               "_under_1000MWh_" +
                                                                                               self.trend]) * \
                                                                 min(1000, electric_consumption.at[
                                                                     i, 'electric_consumption_' + self.technology +
                                                                     '_' + str(self.size) + '_' + self.trend]) * 10

                    self.opex_data.at[i, 'el_cost_over_1000'] = float(self.purchase_prices.at[i, self.sector +
                                                                                              "_over_1000MWh_" +
                                                                                              self.trend]) * \
                        max(0, electric_consumption.at[i, 'electric_consumption_' + self.technology + '_' +
                                                       str(self.size) + '_' + self.trend] - 1000) * 10
        else:
            for i in self.opex_data.index:
                self.opex_data.at[i, 'el_cost_under_1000'] = float(self.purchase_prices.at[i, self.el_source +
                                                                                           "_under_1000MWh_" +
                                                                                           self.trend]) * \
                                                             min(1000, electric_consumption.at[
                                                                 i, 'electric_consumption_' + self.technology +
                                                                 '_' + str(self.size) + '_' + self.trend]) * 10

                self.opex_data.at[i, 'el_cost_over_1000'] = float(self.purchase_prices.at[i, self.el_source +
                                                                                          '_' +
                                                                                          self.buy_price +
                                                                                          "_over_1000MWh_" +
                                                                                          self.trend]) * \
                    max(0, electric_consumption.at[i, 'electric_consumption_' + self.technology + '_' +
                                                   str(self.size) + '_' + self.trend] - 1000) * 10

                if self.el_source == 'self-consumption':
                    if flh.at[i, 'flh_' + self.technology + '_' + str(self.size) + '_' + self.trend] > 3100:
                        d = float(self.purchase_prices.at[i, "grid_full_over_1000MWh_" + self.trend]) - \
                            float(self.purchase_prices.at[i, "self-consumption_energy_intensive_over_1000MWh_" +
                                                          self.trend])
                        self.opex_data.at[i, 'surcharge_3100_flh'] = d * 10 * self.size * \
                            max(0, flh.at[i, 'flh_' + self.technology + '_' + str(self.size) + '_' + self.trend] - 3100)

        self.opex_data['opex_el_total'] = self.opex_data['el_cost_over_1000'] + self.opex_data['el_cost_under_1000'] + \
            self.opex_data['surcharge_3100_flh']

        return self.opex_data
