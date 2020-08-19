"""
This file contains the loop for the calculation of the IRR, is slow at the moment, the plan for future is to
parallelize it
"""

import numpy as np
import scipy.optimize as opt
import time
import math
import modules.generate_sector_classes as generate_class
from modules.calc_hist_diffusion import HistoricDiffusion
import modules.calc_installed_cap_from_hist as icfh
import modules.calc_annual_diffusion as ad
from modules.IRR.calc_investment import CalcInvestment
from modules.IRR.calc_operational_cost import CalcOperationalCost
from modules.IRR.calc_financial_expenses import CalcFinancialExpenses
from modules.IRR.calc_income_statement import CalcIncomeStatement
from modules.IRR.calc_cashflow import CalcCashflow


MAX_LOG_RATE = 1e3
BASE_TOL = 1e-12


def loop(cap_max, share_sector, sector_sizes, year_start, duration, debt_share, debt_term, debt_interest_rate,
         income_tax, ptg_data):
    """
    First the data frames for the sectors are generated, then for each sector the rate for a logistic function matching
    the historical development and the maximal capacity is calculated. With this rate the annual capacities are
    calculated which give the annual growth rate. Then the loop for the calculation of the IRR is started.
    :param cap_max: maximal installed capacity overall
    :param share_sector: shares of the sectors of the overall capacity
    :param sector_sizes: sizes of the facilities under consideration for the single sectors
    :param year_start: year in which the first facilities were constructed
    :param duration: duration until the maximal capacity is reached
    :param debt_share: part of debt in financing
    :param debt_term: runtime of debt
    :param debt_interest_rate: interest rate of debt
    :param income_tax: income tax
    :param ptg_data: general data like investment cost, efficiency and so on, see read_and_generate_data.py for details
    :return: logistic function matching historic development and IRR
    """
    start_loop = time.time()
    mobility_data = generate_class.Mobility(year_start, duration)
    industry_data = generate_class.Industry(year_start, duration)
    injection_data = generate_class.Injection(year_start, duration)
    re_electrification_data = generate_class.ReElectrification(year_start, duration)

    sector_data = {}

    for sector in ['mobility', 'industry', 'injection', 're_electrification']:
        # -------Calculation of diffusion rate from historic data
        cap_max_sector = cap_max * share_sector[sector]
        locals()[sector + '_data'].cap_max_sector = float(cap_max_sector)
        hd = HistoricDiffusion(ptg_data.hist[sector], sector, duration, cap_max_sector)

        # direct minimization
        s = opt.minimize(hd.function_to_minimize, 0.5)
        rate_hist = s.x.squeeze()
        locals()[sector + '_data'].rate_hist = float(rate_hist)

        # -------Calculation of installed power with rate from historic data
        locals()[sector + '_data'].cap_installed_hist = icfh.calc_installed_cap(year_start, duration,
                                                                                          cap_max_sector, rate_hist)
        # -------Calculation of annual diffusion rate from capacity
        locals()[sector + '_data'].annual_rate = ad.calc_annual_diffusion(year_start, duration, cap_max_sector,
                                                                          cap_installed_hist=locals()[
                                                                              sector + '_data'].cap_installed_hist)

        for year_start_facility in range(2020, 2052):
            loop_year(year_start_facility, sector, sector_sizes, debt_share, debt_term, debt_interest_rate, income_tax,
                      ptg_data, locals()[sector + '_data'])

        print(time.time() - start_loop)

        sector_data[sector] = locals()[sector + '_data']

    return sector_data


def loop_year(year_start_facility, sector, sector_sizes, debt_share, debt_term, debt_interest_rate, income_tax,
              ptg_data, data):
    """
    Calculation of the cash flow which then yields the IRR. Loop for all technologies, sizes and prices
    :param year_start_facility: see loop
    :param sector:see loop
    :param sector_sizes: see loop
    :param debt_share: see loop
    :param debt_term: see loop
    :param debt_interest_rate: see loop
    :param income_tax: see loop
    :param ptg_data: see loop
    :param data: specific data frames for sector
    :return: IRR
    """
    for technology in ['AEL', 'PEM']:
        for size in sector_sizes[sector]:
            for trend in ['pessimistic', 'optimistic']:
                for el_source in ['grid', 'self-consumption']:
                    for buy_price in ['full', 'energy_intensive']:
                        if el_source == 'self-consumption' and buy_price == 'energy_intensive':
                            continue
                        # -------Calculation of investment costs
                        ci = CalcInvestment(year_start_facility, sector, technology, size, trend,
                                            ptg_data.investment_sys, ptg_data.tech_param,
                                            ptg_data.investment_other)
                        investment = ci.calc_invest()

                        # -------Calculation of operation cost
                        coc = CalcOperationalCost(investment, sector, year_start_facility, technology, size,
                                                  el_source, trend, buy_price, ptg_data.opex,
                                                  ptg_data.purchase_prices)
                        coc.calc_equipment_opex()
                        opex = coc.calc_electricity_opex(flh=ptg_data.full_load_hours,
                                                         electric_consumption=ptg_data.electric_consumption)

                        # -------Calculation of financial expenses
                        cfe = CalcFinancialExpenses(investment, year_start_facility, opex, debt_share,
                                                    debt_term,
                                                    debt_interest_rate)

                        amortization, interest = cfe.calc_financial_expenses()

                        # -------Calculation of taxes
                        cis = CalcIncomeStatement(ptg_data.revenue['revenue_' + sector + '_' + str(size) + '_' + trend],
                                                  opex, interest, investment, income_tax, ptg_data.tech_param,
                                                  technology)

                        income = cis.calc_income()

                        # -------Calculation of cashflow

                        cc = CalcCashflow(ptg_data.revenue['revenue_' + sector + '_' + str(size) + '_' + trend],
                                          investment, year_start_facility, opex, income, debt_share, amortization,
                                          interest)

                        cashflow = cc.calc_cashflow()

                        # -------Calculation of irr
                        # nan is set to 0

                        irr_financial = np.irr(cashflow['financial'])

                        if math.isnan(irr_financial):
                            irr_financial = 0.

                        data.irr.at[
                            year_start_facility - 1, sector + '_' + technology + '_' +
                            str(size) + '_' + trend + '_' + buy_price + '_' +
                            el_source] = irr_financial
