import pandas as pd
import numpy as np
import plotly.express as px


def plot(sector_data):
    """
    Plotting of the irr per sector
    :param sector_data:
    :return:
    """
    industry = sector_data['industry'].irr
    injection = sector_data['injection'].irr
    mobility = sector_data['mobility'].irr
    re_electrification = sector_data['re_electrification'].irr
    # initialize parameters
    n_rows = 32
    n_cols_new = 5
    col_names = ['year', 'sector', 'tech', 'size', 'tech+size', 'opti_pessi', 'tarif', 'info', 'irr']
    years = list(range(2019, 2051))  # for all
    tech1 = list(['AEL'] * 12 * n_rows + ['PEM'] * 12 * n_rows)  # ind,mob,inj
    tech2 = list(['AEL'] * 18 * n_rows + ['PEM'] * 18 * n_rows)  # ree
    size1 = list([3.1] * 6 * n_rows + [10] * 6 * n_rows + [3.1] * 6 * n_rows + [10] * 6 * n_rows)  # ind, mob
    size2 = list([10] * 6 * n_rows + [590] * 6 * n_rows + [10] * 6 * n_rows + [590] * 6 * n_rows)  # inj
    size3 = list([10] * 6 * n_rows + [310] * 6 * n_rows + [590] * 6 * n_rows + [10] * 6 * n_rows + [310] * 6 * n_rows +
                 [590] * 6 * n_rows)  # ree
    tarif = list(["full_grid"] * n_rows + ["energy_intensive_grid"] * n_rows + ["full_self-consumption"] * n_rows)
    # for all
    opti_pessi = list(['pessimistic'] * 3 * n_rows + ['optimistic'] * 3 * n_rows)  # for all

    # create new dataframes for each sector from csv data
    # industry df
    n_cols = len(industry.columns)
    n_rows_new = n_rows * n_cols

    ind_new = pd.DataFrame(columns=col_names, index=np.arange(n_rows_new))
    ind_new['year'] = years * int((ind_new.shape[0] / len(years)))
    ind_new['sector'][:len(ind_new)] = "industry"
    ind_new['tech'] = tech1
    ind_new['size'] = size1
    ind_new['tarif'] = tarif * int((ind_new.shape[0] / len(tarif)))
    ind_new['opti_pessi'] = opti_pessi * int((ind_new.shape[0] / len(opti_pessi)))

    for i in range(ind_new.shape[0]):
        ind_new['info'][i] = ind_new['tech'][i] + '_' + str(ind_new['size'][i]) + '_' + ind_new['opti_pessi'][i]
    for i in range(ind_new.shape[0]):
        ind_new['tech+size'][i] = ind_new['tech'][i] + '_' + str(ind_new['size'][i])
    z = 0
    for j in range(1, n_cols):
        for i in range(len(years)):
            ind_new.iat[z, ind_new.shape[1] - 1] = industry.iloc[i, j]
            z = z + 1

    ind_new['tarif'] = ind_new['tarif'].astype("category")
    ind_new['irr'] = pd.to_numeric(ind_new['irr'])

    # injection df
    n_cols = len(injection.columns)
    n_rows_new = n_rows * n_cols

    inj_new = pd.DataFrame(columns=col_names, index=np.arange(n_rows_new))

    inj_new['year'] = years * int((inj_new.shape[0] / len(years)))
    inj_new['sector'][:len(inj_new)] = "injection"
    inj_new['tech'] = tech1
    inj_new['size'] = size2
    inj_new['tarif'] = tarif * int((inj_new.shape[0] / len(tarif)))
    inj_new['opti_pessi'] = opti_pessi * int((inj_new.shape[0] / len(opti_pessi)))
    for i in range(inj_new.shape[0]):
        inj_new['info'][i] = inj_new['tech'][i] + '_' + str(inj_new['size'][i]) + '_' + inj_new['opti_pessi'][i]
    for i in range(inj_new.shape[0]):
        inj_new['tech+size'][i] = inj_new['tech'][i] + '_' + str(inj_new['size'][i])
    z = 0
    for j in range(1, n_cols):
        for i in range(len(years)):
            inj_new.iat[z, inj_new.shape[1] - 1] = injection.iloc[i, j]
            z = z + 1

    inj_new['tarif'] = inj_new['tarif'].astype("category")
    inj_new['irr'] = pd.to_numeric(inj_new['irr'])

    # mobility df
    n_cols = len(mobility.columns)
    n_rows_new = n_rows * n_cols

    mob_new = pd.DataFrame(columns=col_names, index=np.arange(n_rows_new))

    mob_new['year'] = years * int((mob_new.shape[0] / len(years)))
    mob_new['sector'][:len(mob_new)] = "mobility"
    mob_new['tech'] = tech1
    mob_new['size'] = size1
    mob_new['tarif'] = tarif * int((mob_new.shape[0] / len(tarif)))
    mob_new['opti_pessi'] = opti_pessi * int((mob_new.shape[0] / len(opti_pessi)))
    for i in range(mob_new.shape[0]):
        mob_new['info'][i] = mob_new['tech'][i] + '_' + str(mob_new['size'][i]) + '_' + mob_new['opti_pessi'][i]
    for i in range(mob_new.shape[0]):
        mob_new['tech+size'][i] = mob_new['tech'][i] + '_' + str(mob_new['size'][i])
    z = 0
    for j in range(1, n_cols):
        for i in range(len(years)):
            mob_new.iat[z, mob_new.shape[1] - 1] = mobility.iloc[i, j]
            z = z + 1

    mob_new['tarif'] = mob_new['tarif'].astype("category")
    mob_new['irr'] = pd.to_numeric(mob_new['irr'])

    # re_electrification df
    n_cols = len(re_electrification.columns)
    n_rows_new = n_rows * n_cols

    ree_new = pd.DataFrame(columns=col_names, index=np.arange(n_rows_new))

    ree_new['year'] = years * int((ree_new.shape[0] / len(years)))
    ree_new['sector'][:len(ree_new)] = "re_electrification"
    ree_new['tech'] = tech2
    ree_new['size'] = size3
    ree_new['tarif'] = tarif * int((ree_new.shape[0] / len(tarif)))
    ree_new['opti_pessi'] = opti_pessi * int((ree_new.shape[0] / len(opti_pessi)))
    for i in range(ree_new.shape[0]):
        ree_new['info'][i] = ree_new['tech'][i] + '_' + str(ree_new['size'][i]) + '_' + ree_new['opti_pessi'][i]
    for i in range(ree_new.shape[0]):
        ree_new['tech+size'][i] = ree_new['tech'][i] + '_' + str(ree_new['size'][i])
    z = 0
    for j in range(1, n_cols):
        for i in range(len(years)):
            ree_new.iat[z, ree_new.shape[1] - 1] = re_electrification.iloc[i, j]
            z = z + 1

    ree_new['tarif'] = ree_new['tarif'].astype("category")
    ree_new['irr'] = pd.to_numeric(ree_new['irr'])

    # barplot for mobility
    fig = px.box(mob_new, x='year', y='irr', color='tech+size', facet_row='tarif')
    fig.update_layout(title_text="Mobility")
    fig.update_yaxes(title="IRR of fsc", row=1, col=1)
    fig.update_yaxes(title="IRR of eig", row=2, col=1)
    fig.update_yaxes(title="IRR of fg", row=3, col=1)
    # fig.show()
    fig.write_html('plots/bar_mobility.html', auto_open=True)

    # barplot for industry
    fig = px.box(ind_new, x='year', y='irr', color='tech+size', facet_row='tarif')
    fig.update_layout(title_text="Industry")
    fig.update_yaxes(title="IRR of fsc", row=1, col=1)
    fig.update_yaxes(title="IRR of eig", row=2, col=1)
    fig.update_yaxes(title="IRR of fg", row=3, col=1)
    # fig.show()
    fig.write_html('plots/bar_industry.html', auto_open=True)

    # barplot for injection
    fig = px.box(inj_new, x='year', y='irr', color='tech+size', facet_row='tarif')
    fig.update_layout(title_text="Injection")
    fig.update_yaxes(title="IRR of fsc", row=1, col=1)
    fig.update_yaxes(title="IRR of eig", row=2, col=1)
    fig.update_yaxes(title="IRR of fg", row=3, col=1)
    # fig.show()
    fig.write_html('plots/bar_injection.html', auto_open=True)

    # barplot for re-electr.
    fig = px.box(ree_new, x='year', y='irr', color='tech+size', facet_row='tarif')
    fig.update_layout(title_text="Re-electrification")
    fig.update_yaxes(title="IRR of fsc", row=1, col=1)
    fig.update_yaxes(title="IRR of eig", row=2, col=1)
    fig.update_yaxes(title="IRR of fg", row=3, col=1)
    # fig.show()
    fig.write_html('plots/bar_re-electr.html', auto_open=True)
