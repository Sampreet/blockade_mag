# dependencies
import numpy as np

# qom modules
from qom.ui.plotters import MPLPlotter

# system parameters
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
data = np.load('data/v2.6_qutip-v4.7.3/7_' + '_'.join([str(param) for param in [N, kappa, gamma, delta_q, delta_1, delta_2, g_1, g_2, Omega, dim]]) + '.npz')
Ts = data['arr_0']
G_2_0s.append(data['arr_1'])

# load data for finite detuning
delta_q = 0.1 * kappa
delta_1 = -0.276 * kappa
delta_2 = 0.1 * kappa
g_2 = 0.137 * g_1
data = np.load('data/v2.6_qutip-v4.7.3/7_' + '_'.join([str(param) for param in [N, kappa, gamma, delta_q, delta_1, delta_2, g_1, g_2, Omega, dim]]) + '.npz')
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
        'x_label'           : '$T$ (mK)',
        'x_tick_labels'     : [i + 1 for i in range(6)],
        'x_ticks'           : [i * 1e-3 + 1e-3 for i in range(6)],
        'x_ticks_minor'     : [i * 0.2e-3 + 1e-3 for i in range(26)],
        'x_scale'           : 'linear',
        'v_label'           : '$g^{(2)} (0)$',
        'v_limits'          : [10**(- 5), 10],
        'v_scale'           : 'log',
        'v_tick_labels'     : ['$10^{' + str(i * 2 - 4) + '}$' for i in range(3)],
        'v_ticks'           : [10**(i * 2 - 4) for i in range(3)],
        'v_ticks_minor'     : [10**(i - 5) for i in range(7)],
        'show_legend'       : True,
        'legend_labels'     : ['$\\delta_{j} = 0$', '$\\delta_{j} \\neq 0$'],
        'legend_location'   : 'center left',
        'label_font_size'   : 24,
        'legend_font_size'  : 20,
        'tick_font_size'    : 20,
        'width'             : 6.4,
        'height'            : 3.0
    }
)
plotter.update(
    vs=G_2_0s + [[1] * len(Ts)],
    xs=Ts
)
plotter.show()