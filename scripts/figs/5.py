from qom.ui.plotters import MPLPlotter
import numpy as np
import os
import sys
import time

# add path to local libraries
sys.path.append(os.path.abspath(os.path.join('..', 'blockade_mag')))
# import function
from common.g_2_0 import *

# params
N       = 5
kappa   = 1.0
gamma   = 1.11 * kappa
g_1     = 0.8 * kappa
Omega   = 1e-3 * kappa
dim_1   = 1001
dim_2   = 251
dim_3   = 251
load    = True

if not load:
    # initialize
    delta_1s= np.linspace(-1.0, 0.0, dim_1) * kappa
    g_2s    = np.linspace(0.05, 0.30, dim_2) * g_1
    delta_qs= np.linspace(0.0, 0.25, dim_2) * kappa
    start   = time.time()
    vs      = list()

    # find all conditions
    conditions = list()
    for i in range(len(delta_qs)):
        # display
        time_elapsed = time.time() - start
        progress = i / (dim_2 - 1) * 100
        print('\r{:0.3f}s\t'.format(time_elapsed) + ('\t' if time_elapsed < 100.0 else '') + 'Progress: {:0.2f}%'.format(progress), end='\t')

        # update detunings
        delta_q = delta_qs[i]
        delta_2 = delta_q

        # iterate
        conditions_temp = list()
        vs_a_temp = list()
        for g_2 in g_2s:
            # calculate conditions
            temp = list()
            for delta_1 in delta_1s:
                temp.append(get_condition([kappa, gamma, delta_q, delta_1, delta_2, g_1, g_2, Omega]))
            conditions_temp.append(temp)
        conditions.append(conditions_temp)

    # save data
    np.savez_compressed('data/figs/5_' + '_'.join([str(param) for param in [kappa, gamma, g_1, Omega, dim_1, dim_2, dim_3]]), delta_1s, g_2s, delta_qs, conditions)

# load data
else:
    data        = np.load('data/figs/5_' + '_'.join([str(param) for param in [kappa, gamma, g_1, Omega, dim_1, dim_2, dim_3]]) + '.npz')
    delta_1s    = data['arr_0']
    g_2s        = data['arr_1']
    delta_qs    = data['arr_2']
    conditions  = data['arr_3']
    vs          = list()
    # find positions
    for i in range(dim_3):
        vs_temp = list()
        for j in range(dim_2):
            vs_temp.append(delta_1s[np.argmin(conditions[i][j])])
        vs.append(vs_temp)

# plotter
plotter = MPLPlotter(axes={
    'X': g_2s / g_1, 
    'Y': delta_qs[::100]
}, params={
    'type': 'lines',
    'palette': 'RdBu',
    'bins': 41,
    'x_label': '$g_{2} / g_{1}$',
    'x_tick_labels': ['{:0.2f}'.format(i * 0.05 + 0.05) for i in range(6)],
    # 'x_tick_position': 'bottom-out',
    'x_ticks': [i * 0.05 + 0.05 for i in range(6)],
    'x_ticks_minor': [i * 0.01 + 0.05 for i in range(26)],
    # 'y_label': '$\\delta_{q} / \\kappa$, $\\delta_{2} / \\kappa$',
    # 'y_tick_labels': ['{:0.2f}'.format(i * 0.05) for i in range(6)],
    # 'y_tick_position': 'left-out',
    # 'y_ticks': [i * 0.05 for i in range(6)],
    # 'y_ticks_minor': [i * 0.01 for i in range(26)],
    # 'show_cbar': True,
    # 'cbar_title': '$\\delta_{1} / \\kappa$',
    # 'cbar_tick_labels': [f'{i * 0.1 - 0.7:0.1f}' for i in range(8)],
    # 'cbar_ticks': [i * 0.1 - 0.7 for i in range(8)],
    'y_name': '$\\delta_{q} / \\kappa$',
    'y_colors': ['k', -1, 0],
    'v_label': '$\\delta_{1_{\\mathrm{opt}}} / \\kappa$',
    'v_limits': [-0.7, 0.3],
    'v_tick_labels': [f'{i * 0.4 - 0.6:0.1f}' for i in range(3)],
    'v_ticks': [i * 0.4 - 0.6 for i in range(3)],
    'v_ticks_minor': [i * 0.1 - 0.7 for i in range(9)],
    'show_legend': True,
    'legend_location': 'lower right',
    'height': 3.0,
    'width': 6.4,
    'label_font_size': 24,
    'legend_font_size': 20,
    'tick_font_size': 20
})
plotter.update(xs=g_2s / g_1, vs=vs[::100])
plotter.show(True)