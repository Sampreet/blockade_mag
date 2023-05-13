from qom.ui.plotters import MPLPlotter
import numpy as np
import os
import sys

# add path to local libraries
sys.path.append(os.path.abspath(os.path.join('..', 'blockade_mag')))
# import function
from common.g_2_0 import *

# parameters
N       = 5
kappa   = 1.0
gamma   = 1.11 * kappa
# gamma   = 1.1 * kappa # alt
delta_q = 0.0 * kappa
delta_2 = 0.0 * kappa
g_1     = 0.8 * kappa
Omega   = 1e-3 * kappa
dim_1   = 201
dim_2   = 201

# load data
data    = np.load('data/figs/3_' + '_'.join([str(param) for param in [N, kappa, gamma, delta_q, delta_2, g_1, Omega, dim_1, dim_2]]) + '.npz')
X       = data['arr_0']
Y       = data['arr_1']
g_2_0s  = data['arr_2']

# data points
xs      = X[0]
ys      = [y[0] for y in Y[100:130:10]]
# ys      = [y[0] for y in Y[110:140:10]] # alt
vs_a    = list()
xs_n    = xs[::5]
vs_n    = [v[::5] for v in g_2_0s[100:130:10]]
# vs_n    = [v[::5] for v in g_2_0s[110:140:10]] # alt
for g_2_g_1_ratio in ys:
    # update coupling strength
    g_2 = g_2_g_1_ratio * g_1
    g_2_0s_temp = list()
    for delta_1_norm in xs:
        # update magnon detuning
        delta_1 = delta_1_norm * kappa

        # update correlations
        g_2_0 = get_g_2_0_simplified([kappa, gamma, delta_q, delta_1, delta_2, g_1, g_2, Omega])
        g_2_0s_temp.append(g_2_0)
    vs_a.append(g_2_0s_temp)

# plotter
plotter = MPLPlotter(axes={
    'X': xs,
    'Y': [f'{y:0.2f}' for y in ys]
}, params={
    'type': 'lines',
    'palette': 'RdBu_r',
    'bins': 11,
    'x_label': '$\\delta_{1} / \\kappa$',
    'x_tick_labels': ['{:0.2f}'.format(i * 0.05 - 0.1) for i in range(5)],
    'x_ticks': [i * 0.05 - 0.1 for i in range(5)],
    'x_ticks_minor': [i * 0.01 - 0.1 for i in range(21)],
    'y_name': '$g_{2} / g_{1}$',
    'y_colors': [0, 'k', -1],
    'y_sizes': [1, 1, 1],
    'v_label': '$g^{(2)} (0)$',
    'v_limits': [10**(-7), 10**(-1)],
    'v_scale': 'log',
    'v_tick_labels': ['$10^{' + str(i * 2 - 6) + '}$' for i in range(3)],
    'v_ticks': [10**(i * 2 - 6) for i in range(3)],
    'v_ticks_minor': [10**(i - 7) for i in range(7)],
    'show_legend': True,
    'legend_location': 'lower right',
    'height': 3.0,
    'width': 6.4,
    'label_font_size': 24,
    'legend_font_size': 20,
    'tick_font_size': 20,
    'annotations': [{
        's': '(b)',
        'xy': (0.23, 0.39),
        'font_dict': 'label',
        'color': 'k'
    }]
})
plotter.update(xs=xs, ys=ys, vs=vs_a)
# additional lines
ax      = plotter.get_current_figure().axes[0]
colors  = plotter.get_colors(palette='RdBu_r', bins=11)
ax.scatter(xs_n, vs_n[0], s=25, marker='o', color=colors[1])
ax.scatter(xs_n, vs_n[1], s=25, marker='x', color='k')
ax.scatter(xs_n, vs_n[2], s=25, marker='s', color=colors[-2])
# ax.plot(X[0], [pos_1[1]] * len(X[0]), linestyle='--', linewidth=1, color=colors[-2])
# ax.scatter([pos_1[0]], [pos_1[1]], s=100, marker='o', facecolors='none', edgecolors='k')
# ax.plot([pos_2[0]] * len(Y[:, 0]), Y[:, 0], linestyle='--', linewidth=1, color=colors[-2])
# ax.plot(X[0], [pos_2[1]] * len(X[0]), linestyle='--', linewidth=1, color=colors[1])
# ax.scatter([pos_2[0]], [pos_2[1]], s=100, marker='o', facecolors='none', edgecolors='k')
plotter.show(True)