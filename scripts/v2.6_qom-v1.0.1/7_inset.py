# dependencies
import numpy as np

# qom modules
from qom.ui.plotters import MPLPlotter

# parameters
N       = 5
kappa   = 1.0
gamma   = 1.11 * kappa
g_1     = 0.8 * kappa
Omega   = 1e-3 * kappa
dim     = 251

# initialize
G_2_0s = list()

# load data for zero detuning
delta_q = 0.0 * kappa
delta_1 = 0.0 * kappa
delta_2 = 0.0 * kappa
g_2 = 0.161 * g_1
data = np.load('data/v2.6_qom-v1.0.1/7_' + '_'.join([str(param) for param in [N, kappa, gamma, delta_q, delta_1, delta_2, g_1, g_2, Omega, dim]]) + '.npz')
Ts = data['arr_0']
G_2_0s.append(data['arr_1'])

# load data for finite detuning
delta_q = 0.1 * kappa
delta_1 = -0.276 * kappa
delta_2 = 0.1 * kappa
g_2 = 0.137 * g_1
data = np.load('data/v2.6_qom-v1.0.1/7_' + '_'.join([str(param) for param in [N, kappa, gamma, delta_q, delta_1, delta_2, g_1, g_2, Omega, dim]]) + '.npz')
G_2_0s.append(data['arr_1'])

# plotter
plotter = MPLPlotter(
    axes={},
    params={
        'type'              : 'lines',
        'bins'              : 11,
        'colors'            : [0, -1, 'k'],
        'sizes'             : [2, 2, 1],
        'styles'            : ['-', '-.', '--'],
        'x_label'           : '',
        'x_tick_labels'     : [i * 0.2 + 2 for i in range(3)],
        'x_ticks'           : [i * 0.2e-3 + 2e-3 for i in range(3)],
        'x_ticks_minor'     : [i * 0.1e-3 + 2e-3 for i in range(5)],
        'x_scale'           : 'linear',
        'v_label'           : '',
        'v_limits'          : [2 * 10**(-5), 5 * 10**(-5)],
        'v_scale'           : 'linear',
        'v_tick_labels'     : [str(i + 2) + '$\\times 10^{-5}$' for i in range(4)],
        'v_ticks'           : [(i + 2) * 10**(-5) for i in range(4)],
        'v_ticks_minor'     : [(i * 0.5 + 2) * 10**(-5) for i in range(7)],
        'label_font_size'   : 20,
        'legend_font_size'  : 16,
        'tick_font_size'    : 16,
        'width'             : 2.0,
        'height'            : 1.6
    }
)
plotter.update(
    vs=G_2_0s + [[1] * len(Ts)],
    xs=Ts
)
plotter.show()