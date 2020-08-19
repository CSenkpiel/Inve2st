import pandas as pd


def calc_annual_diffusion(year_start, duration, cap_max_sector, cap_installed_hist):
    """
    Calculation of the annual diffusion rate from installed capacities calculated in calc_installed_cap_from_hist.py.
    These rates are later dampened by the determinants.
    :param year_start: year in which the first facility started
    :param duration: period of time until the maximum capacity is installed
    :param  cap_max_sector: maximum capacity in the sector under consideration
    :param cap_installed_hist: the computed installed capacities from the historical development
    :return: data frame with growth rates
    """
    rate = pd.DataFrame(index=range(year_start, year_start + duration), columns=['annual_rate'])
    for i in range(duration):
        if i == 0:
            r = 0
        else:
            r = (cap_installed_hist.at[year_start + i, 'capacity'] -
                 cap_installed_hist.at[year_start + i - 1, 'capacity']) / \
                (cap_installed_hist.at[year_start + i - 1, 'capacity'] *
                 (1 - cap_installed_hist.at[year_start + i - 1, 'capacity'] / cap_max_sector))
        rate.at[year_start + i, 'annual_rate'] = r
    return rate
