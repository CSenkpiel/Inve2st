"""
In this file the annual capacity with the dampened rates is calculated
"""
import pandas as pd


def calc_modified_capacity(sector_data, cap_max, share_sector):
    """
    Calculation of the modified annual capacity by logistic function
    :param sector_data: sector data
    :param cap_max: maximum capacity (undampened)
    :param share_sector: percentage of sectors of cap_max
    :return: dampened capacities
    """
    for sector in ['mobility', 'industry', 'injection', 're_electrification']:
        cap = pd.DataFrame(index=range(2009, 2051), columns=['capacity_optimistic', 'annex_optimistic',
                                                             'capacity_pessimistic', 'annex_pessimistic',
                                                             'capacity_max', 'annex_max',
                                                             'capacity_min', 'annex_min',
                                                             'capacity_mean', 'annex_mean'])
        cap_max_sector = cap_max * share_sector[sector]
        for i in cap.index:
            if i < 2020:
                cap.at[i, 'capacity_optimistic'] = sector_data[sector].cap_installed_hist.at[i, 'capacity']
                cap.at[i, 'capacity_pessimistic'] = sector_data[sector].cap_installed_hist.at[i, 'capacity']
                cap.at[i, 'capacity_max'] = sector_data[sector].cap_installed_hist.at[i, 'capacity']
                cap.at[i, 'capacity_min'] = sector_data[sector].cap_installed_hist.at[i, 'capacity']
                cap.at[i, 'capacity_mean'] = sector_data[sector].cap_installed_hist.at[i, 'capacity']

            else:
                c_opt = sector_data[sector].new_rate.at[i, 'rate_optimistic'] * cap.at[i - 1, 'capacity_optimistic'] * \
                        (1 - cap.at[i - 1, 'capacity_optimistic'] / cap_max_sector) + cap.at[i - 1,
                                                                                             'capacity_optimistic']
                cap.at[i, 'capacity_optimistic'] = c_opt
                c_pess = sector_data[sector].new_rate.at[i, 'rate_pessimistic'] * \
                    cap.at[i - 1, 'capacity_pessimistic'] * (1 - cap.at[i - 1, 'capacity_pessimistic'] /
                                                             cap_max_sector) + cap.at[i - 1, 'capacity_pessimistic']
                cap.at[i, 'capacity_pessimistic'] = c_pess
                c_max = sector_data[sector].new_rate.at[i, 'rate_max'] * cap.at[i - 1, 'capacity_max'] * \
                    (1 - cap.at[i - 1, 'capacity_max'] / cap_max_sector) + cap.at[i - 1, 'capacity_max']
                cap.at[i, 'capacity_max'] = c_max
                c_min = sector_data[sector].new_rate.at[i, 'rate_min'] * cap.at[i - 1, 'capacity_min'] * \
                    (1 - cap.at[i - 1, 'capacity_min'] / cap_max_sector) + cap.at[i - 1, 'capacity_min']
                cap.at[i, 'capacity_min'] = c_min
                c_mean = sector_data[sector].new_rate.at[i, 'rate_mean'] * cap.at[i - 1, 'capacity_mean'] * \
                    (1 - cap.at[i - 1, 'capacity_mean'] / cap_max_sector) + cap.at[i - 1, 'capacity_mean']
                cap.at[i, 'capacity_mean'] = c_mean

            if i > 2009:
                cap.at[i, 'annex_optimistic'] = cap.at[i, 'capacity_optimistic'] - cap.at[i - 1, 'capacity_optimistic']
                cap.at[i, 'annex_pessimistic'] = cap.at[i, 'capacity_pessimistic'] - \
                    cap.at[i - 1, 'capacity_pessimistic']
                cap.at[i, 'annex_max'] = cap.at[i, 'capacity_max'] - cap.at[i - 1, 'capacity_max']
                cap.at[i, 'annex_min'] = cap.at[i, 'capacity_min'] - cap.at[i - 1, 'capacity_min']
                cap.at[i, 'annex_mean'] = cap.at[i, 'capacity_mean'] - cap.at[i - 1, 'capacity_mean']

        sector_data[sector].capacity = cap.fillna(0)
