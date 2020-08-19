def save_data(sector_data):
    """
    This function saves the relevant data as csv to results folder
    :param sector_data: sector data
    :return:
    """
    capacity = prepare_data(sector_data)
    capacity.to_csv('results/capacity_tot.csv')
    for sector in ['mobility', 'industry', 'injection', 're_electrification']:
        sector_data[sector].capacity.to_csv('results/capacity_' + sector + '.csv')
        sector_data[sector].irr.to_csv('results/irr_' + sector + '.csv')


def prepare_data(sector_data):
    """
    Summation of the sectors capacity to get the overall data
    :param sector_data: sector data
    :return: overall capacity
    """
    capacity_total = sector_data['mobility'].capacity + sector_data['industry'].capacity + \
        sector_data['injection'].capacity + sector_data['re_electrification'].capacity
    return capacity_total
