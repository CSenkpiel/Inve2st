# -*- coding: utf-8 -*-
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio


def plot(sector_data):
    """
    Plotting of the capacity per sector and in total
    :param sector_data:
    :return:
    """
    cap_ind = sector_data['industry'].capacity
    cap_ind_hist = sector_data['industry'].cap_installed_hist
    cap_inj = sector_data['injection'].capacity
    cap_inj_hist = sector_data['injection'].cap_installed_hist
    cap_mob = sector_data['mobility'].capacity
    cap_mob_hist = sector_data['mobility'].cap_installed_hist
    cap_ree = sector_data['re_electrification'].capacity
    cap_ree_hist = sector_data['re_electrification'].cap_installed_hist
    cap_total = cap_mob + cap_ind + cap_inj + cap_ree
    cap_hist = cap_mob_hist + cap_ind_hist + cap_inj_hist + cap_ree_hist
    # Here change saturation point values
    l_mob = list([""]*41+[sector_data['mobility'].cap_max_sector])
    l_ind = list([""]*41+[sector_data['industry'].cap_max_sector])
    l_inj = list([""]*41+[sector_data['injection'].cap_max_sector])
    l_ree = list([""]*41+[sector_data['re_electrification'].cap_max_sector])

    pio.renderers.default = 'browser'
    fig = make_subplots(rows=2, cols=2,
                        subplot_titles=("Mobility", "Injection", "Industry", "Re-electrification"))

    fig.add_trace(go.Scatter(x=cap_mob.index, y=l_mob, mode='markers', marker_color="darkred", showlegend=True,
                             name='Saturation point'), row=1, col=1)

    fig.add_trace(go.Scatter(x=cap_mob.index, y=cap_mob["capacity_max"], line=dict(color='red', dash='dash'),
                             showlegend=True, name='irr_max'), row=1, col=1)

    fig.add_trace(go.Scatter(x=cap_mob.index, y=cap_mob["capacity_optimistic"], mode='lines', marker_color="green",
                             showlegend=True, name='optimistic'), row=1, col=1)

    fig.add_trace(go.Scatter(x=cap_mob.index, y=cap_mob["capacity_pessimistic"], mode='lines', marker_color="orange",
                             showlegend=True, name='pessimistic'), row=1, col=1)

    fig.add_trace(go.Scatter(x=cap_mob.index, y=cap_mob_hist["capacity"], mode='lines', marker_color="black",
                             showlegend=True, name='undampened'), row=1, col=1)

    fig.add_trace(go.Scatter(x=cap_inj.index, y=l_inj, mode='markers', marker_color="darkred", showlegend=False,
                             name='Saturation point'), row=1, col=2)

    fig.add_trace(go.Scatter(x=cap_inj.index, y=cap_inj["capacity_max"], line=dict(color='red', dash='dash'),
                             showlegend=False, name='irr_max'), row=1, col=2)

    fig.add_trace(go.Scatter(x=cap_inj.index, y=cap_inj["capacity_optimistic"], mode='lines', marker_color="green",
                             showlegend=False, name='optimistic'), row=1, col=2)

    fig.add_trace(go.Scatter(x=cap_inj.index, y=cap_inj["capacity_pessimistic"], fill="tonexty", mode='lines',
                             marker_color="orange", showlegend=False, name='pessimistic'), row=1, col=2)

    fig.add_trace(go.Scatter(x=cap_inj.index, y=cap_inj_hist["capacity"], mode='lines', marker_color="black",
                             showlegend=False, name='undampened'), row=1, col=2)

    fig.add_trace(go.Scatter(x=cap_ind.index, y=l_ind, mode='markers', marker_color="darkred", showlegend=False,
                             name='Saturation point'), row=2, col=1)

    fig.add_trace(go.Scatter(x=cap_ind.index, y=cap_ind["capacity_max"], line=dict(color='red', dash='dash'),
                             showlegend=False, name='irr_max'), row=2, col=1)

    fig.add_trace(go.Scatter(x=cap_ind.index, y=cap_ind["capacity_optimistic"], mode='lines', marker_color="green",
                             showlegend=False, name='optimistic'), row=2, col=1)

    fig.add_trace(go.Scatter(x=cap_ind.index, y=cap_ind["capacity_pessimistic"], fill="tonexty", mode='lines',
                             marker_color="orange", showlegend=False, name='pessimistic'), row=2, col=1)

    fig.add_trace(go.Scatter(x=cap_ind.index, y=cap_ind_hist["capacity"], mode='lines', marker_color="black",
                             showlegend=False, name='undampened'), row=2, col=1)

    fig.add_trace(go.Scatter(x=cap_ree.index, y=l_ree, mode='markers', marker_color="darkred", showlegend=False,
                             name='Saturation point'), row=2, col=2)

    fig.add_trace(go.Scatter(x=cap_ree.index, y=cap_ree["capacity_max"], line=dict(color='red', dash='dash'),
                             showlegend=False, name='irr_max'), row=2, col=2)

    fig.add_trace(go.Scatter(x=cap_ree.index, y=cap_ree["capacity_optimistic"], mode='lines', marker_color="green",
                             showlegend=False, fill=None, name='optimistic'), row=2, col=2)

    fig.add_trace(go.Scatter(x=cap_ree.index, y=cap_ree["capacity_pessimistic"], mode='lines', marker_color="orange",
                             showlegend=False, fill="tonexty", name='pessimistic'), row=2, col=2)

    fig.add_trace(go.Scatter(x=cap_ree.index, y=cap_ree_hist["capacity"], mode='lines', marker_color="black",
                             showlegend=False, name='undampened'), row=2, col=2)

    fig.update_yaxes(title="GW", row=1, col=1)
    fig.update_yaxes(title="GW", row=2, col=1)
    fig.update_yaxes(title="GW", row=1, col=2)
    fig.update_yaxes(title="GW", row=2, col=2)

    fig.update_layout(title_text="Simulated diffisuion of Power2Gas", legend=dict(traceorder="grouped"))
    fig.show()

    fig_1 = make_subplots(rows=1, cols=1, subplot_titles="Total capacity")

    fig_1.add_trace(go.Scatter(x=cap_total.index, y=cap_total["capacity_max"], line=dict(color='red', dash='dash'),
                               showlegend=True, name='irr_max'), row=1, col=1)

    fig_1.add_trace(go.Scatter(x=cap_total.index, y=cap_total["capacity_optimistic"], mode='lines', marker_color="green",
                               showlegend=True, name='optimistic'), row=1, col=1)

    fig_1.add_trace(go.Scatter(x=cap_total.index, y=cap_total["capacity_pessimistic"], mode='lines', marker_color="orange",
                               showlegend=True, name='pessimistic'), row=1, col=1)

    fig_1.add_trace(go.Scatter(x=cap_total.index, y=cap_hist["capacity"], mode='lines', marker_color="black",
                               showlegend=True, name='undampened'), row=1, col=1)

    fig_1.update_yaxes(title="GW", row=1, col=1)
    fig_1.update_layout(title_text="Simulated diffisuion of Power2Gas", legend=dict(traceorder="grouped"))
    fig_1.show()
