"""
This is the main file.
"""

import time
from modules.read_and_generate_data import PTGData
import modules.loop as loop
import modules.calc_modified_diffusion as md
import modules.calc_modified_capacity as mc
from modules.save_data import save_data
import modules.plot_irr as plot_irr
import modules.plot_cap as plot_cap


########################################################################################################################
# Settings
########################################################################################################################
# Here the user can set parameters, details in comments

# -------Start year-----------
# this is the year when the first facility was constructed in germany (or at least the first year in
# historic_germany.csv)
year_start = 2009

# -------Duration-------------
# time until maximum capacity is installed (here 2060)
duration = 52

# -------Maximum capacity-----
# target maximum installed capacity in GWel
cap_max = 204

# -------Sector---------------
# sectors: mobility, industry, injection, re_electrification
# share_sectors gives the shares of cap_max the specific sector takes
share_sector = {'mobility': 0.44, 'industry': 0.25, 'injection': 0.22, 're_electrification': 0.09}
# size of the facilities in different sectors in MWel
sector_sizes = {'mobility': [3.1, 10], 'industry': [3.1, 10], 'injection': [10, 590],
                're_electrification': [10, 310, 590]}

# -------financial parameters
# share of debts in financing
debt_share = 0.75
# interest rate for debts
debt_interest_rate = 0.041
# runtime of debts
debt_term = 10
# income tax rate
income_tax = 0.3
# bounds for expectation of investors
upper_bound = 0.3
lower_bound = 0.05

# --------parameters for determinants
# political support
supportive = True
# weights for the sum of the determinants
det_weight = {'economic': 0.6, 'politic': 0.4}
# minimum growth rate without political support
lower_bound_rate = 0.06

# -------Paths
# paths of input csv files
# historic development, only germany available
path_hist = "./inputs/historic_germany.csv"
# sales prices
path_sale = "./inputs/sales_prices.csv"
# investment costs
path_investment_sys = "./inputs/investment_sys.csv"
path_investment_other = "./inputs/investment_other.csv"
# technical_parameters
path_tech = "./inputs/technical_parameters.csv"
# operational cost parameters
path_opex = "./inputs/opex.csv"
# energy cost
path_purchase = "./inputs/energy_purchase.csv"
# political determinants
path_pol = "./inputs/political_determinants.csv"

########################################################################################################################
# Calculations
########################################################################################################################
# for runtime
start_time = time.time()

# read in all data into a class and calculate efficiency and so on, see read_and_generate_data.py
ptg_data = PTGData(path_hist, path_sale, path_investment_sys, path_investment_other, path_tech, path_opex,
                   path_purchase, path_pol)

# loop over years to calculate the cash flow and then the irr
sector_data = loop.loop(cap_max, share_sector, sector_sizes, year_start, duration, debt_share, debt_term,
                        debt_interest_rate, income_tax, ptg_data)

# calculation of the determinants
md.calc_determinant(sector_data, upper_bound, lower_bound, det_weight, ptg_data.pol, lower_bound_rate, supportive)

# calculation of dampened capacity
mc.calc_modified_capacity(sector_data, cap_max, share_sector)

save_data(sector_data)

########################################################################################################################
# Plotting of irr and capacity
########################################################################################################################

plot_irr.plot(sector_data)
plot_cap.plot(sector_data)
print('end of loop ' + str(time.time() - start_time))

pass
