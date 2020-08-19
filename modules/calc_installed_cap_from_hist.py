import pandas as pd
import numpy as np


def calc_installed_cap(year_start, duration, cap_max_sector, rate):
    """
    Here the annual installed capacity is calculated from the historic rates by a logistic function
    :return: data frame with capacities
    """
    cap = pd.DataFrame(index=range(year_start, year_start + duration), columns=['capacity'])
    for i in range(duration):
        c = cap_max_sector / (1 + np.exp(-rate * (i - duration / 2)))
        cap.at[year_start + i, 'capacity'] = c
    return cap
