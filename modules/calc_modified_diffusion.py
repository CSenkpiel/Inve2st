"""
In this file the political and economic determinants are calculated
"""
import pandas as pd


def calc_determinant(sector_data, upper_bound, lower_bound, det_weight, pol_data, lower_bound_rate, supportive):
    """
    Calculation of the determinants to dampen the rates and then calculation of the dampened rates
    :param sector_data: sector specific data
    :param upper_bound: upper bound for the expectation of return
    :param lower_bound: lower bound for the expectation of return
    :param det_weight: weights for the relation of political and financial determinant
    :param pol_data: data frame with the political determinants
    :param lower_bound_rate: minimum growth rate
    :param supportive: True if political decisions are supportive
    :return: determinants and dampened rate
    """
    for sector in ['mobility', 'industry', 'injection', 're_electrification']:
        econ = calc_economic_determinant(sector_data[sector].irr, upper_bound, lower_bound)
        pol = get_political_determinant(sector_data[sector].irr, sector, pol_data, supportive)
        det = calc_det(econ, pol, sector, det_weight, lower_bound_rate)
        det = det.fillna(lower_bound_rate)
        sector_data[sector].new_rate = det.multiply(sector_data[sector].annual_rate[10:42].values)
        sector_data[sector].new_rate = sector_data[sector].new_rate.rename(columns={'determinant_optimistic':
                                                                                    'rate_optimistic',
                                                                                    'determinant_pessimistic':
                                                                                    'rate_pessimistic',
                                                                                    'determinant_max':
                                                                                    'rate_max',
                                                                                    'determinant_min':
                                                                                    'rate_min',
                                                                                    'determinant_mean':
                                                                                    'rate_mean'})
        sector_data[sector].econ = econ
        sector_data[sector].pol = pol


def calc_economic_determinant(data, upper_bound, lower_bound):
    """
    Calculation of economic determinant, it is 1 for irr >= 0.3 and 0 for irr <= 0.05 and linear in the irr in
    between
    :param data: sector data
    :param upper_bound: upper bound for the expectation of return
    :param lower_bound: lower bound for the expectation of return
    :return: economic determinant dataframe
    """
    econ = pd.DataFrame(index=data.index)
    econ['irr_mean'] = data.mean(axis=1)
    econ['irr_max'] = data.max(axis=1)
    econ['irr_min'] = data.min(axis=1)

    data_opt = data[data.columns[data.columns.to_series().str.contains('optimistic')]]
    data_opt.fillna(0)
    econ['irr_optimistic'] = data_opt.mean(axis=1)

    data_pess = data[data.columns[data.columns.to_series().str.contains('pessimistic')]]
    data_pess.fillna(0)
    econ['irr_pessimistic'] = data_pess.mean(axis=1)

    for i in econ.index:
        econ.at[i, 'd_econ_optimistic'] = min(max((econ.at[i, 'irr_optimistic'] - lower_bound) /
                                                  (upper_bound - lower_bound), 0), 1)
        econ.at[i, 'd_econ_pessimistic'] = min(max((econ.at[i, 'irr_pessimistic'] - lower_bound) /
                                                   (upper_bound - lower_bound), 0), 1)
        econ.at[i, 'd_econ_max'] = min(max((econ.at[i, 'irr_max'] - lower_bound) / (upper_bound - lower_bound), 0), 1)
        econ.at[i, 'd_econ_min'] = min(max((econ.at[i, 'irr_min'] - lower_bound) / (upper_bound - lower_bound), 0), 1)
        econ.at[i, 'd_econ_mean'] = min(max((econ.at[i, 'irr_mean'] - lower_bound) / (upper_bound - lower_bound), 0), 1)

    return econ


def get_political_determinant(data, sector, pol_data, supportive):
    """
    Import of the political determinants from csv
    :param data: sector data
    :param sector: sector
    :param pol_data: political determinants
    :param supportive: True if political decisions are supportive
    :return: political determinants dataframe
    """
    pol = pd.DataFrame(0., columns=[sector], index=data.index)

    if supportive:
        for i in pol.index:
            if i < 2022:
                pol.at[i, sector] = 0.
            elif i in range(2022, 2030):
                pol.at[i, sector] = pol_data.at[2022, sector]
            else:
                pol.at[i, sector] = pol_data.at[2030, sector]

    return pol


def calc_det(econ, pol, sector, det_weight, lower_bound_rate):
    """
    Calculation of the overall determinant, it is at least the lower_bound_rate and above the weighted sum of the
    political and economic determinant
    :param econ: economic determinant
    :param pol: political determinant
    :param sector: sector
    :param det_weight: weights for the relation of political and financial determinant
    :param lower_bound_rate: minimum growth rate
    :return: determinant dataframe
    """
    det = pd.DataFrame(index=pol.index)
    for i in det.index:
        det.at[i, 'determinant_optimistic'] = max(lower_bound_rate, det_weight['economic'] *
                                                  econ.at[i, 'd_econ_optimistic'] + det_weight['politic'] *
                                                  pol.at[i, sector])
        det.at[i, 'determinant_pessimistic'] = max(lower_bound_rate, det_weight['economic'] *
                                                   econ.at[i, 'd_econ_pessimistic'] + det_weight['politic'] *
                                                   pol.at[i, sector])
        det.at[i, 'determinant_max'] = max(lower_bound_rate, det_weight['economic'] * econ.at[i, 'd_econ_max'] +
                                           det_weight['politic'] * pol.at[i, sector])
        det.at[i, 'determinant_min'] = max(lower_bound_rate, det_weight['economic'] * econ.at[i, 'd_econ_min'] +
                                           det_weight['politic'] * pol.at[i, sector])
        det.at[i, 'determinant_mean'] = max(lower_bound_rate, det_weight['economic'] * econ.at[i, 'd_econ_mean'] +
                                            det_weight['politic'] * pol.at[i, sector])

    return det
