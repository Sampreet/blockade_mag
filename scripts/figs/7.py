from qom.ui.plotters import MPLPlotter
import numpy as np

# parameters
N       = 5
kappa   = 1.0
gamma   = 1.11 * kappa
g_1     = 0.8 * kappa
Omega   = 1e-3 * kappa
dim     = 201

G_2_0s  = list()

# load data for zero detuning
delta_q = 0.0 * kappa
delta_1 = 0.0 * kappa
delta_2 = 0.0 * kappa
g_2     = 0.161 * g_1
data    = np.load('data/figs/7_' + '_'.join([str(param) for param in [N, kappa, gamma, delta_q, delta_1, delta_2, g_1, g_2, Omega, dim]]) + '.npz')
Ts      = data['arr_0']
G_2_0s.append(data['arr_1'])

# load data for finite detuning
delta_q = 0.1 * kappa
delta_1 = -0.276 * kappa
delta_2 = 0.1 * kappa
g_2     = 0.137 * g_1
data    = np.load('data/figs/7_' + '_'.join([str(param) for param in [N, kappa, gamma, delta_q, delta_1, delta_2, g_1, g_2, Omega, dim]]) + '.npz')
G_2_0s.append(data['arr_1'])

# plotter
plotter = MPLPlotter(axes={
    'X': Ts,
    'Y': ['zero detuning', 'finite detuning']
}, params={
    'type': 'lines',
    'palette': 'RdBu_r',
    'bins': 11,
    'x_label': '$T$ (mK)',
    'x_tick_labels': [i + 2 for i in range(4)],
    'x_ticks': [i * 1e-3 + 2e-3 for i in range(4)],
    'x_ticks_minor': [i * 0.2e-3 + 2e-3 for i in range(16)],
    'x_scale': 'linear',
    'y_colors': [0, -1],
    'y_sizes': [2, 2],
    'y_styles': ['-', '-'],
    'v_label': '$g^{(2)} (0)$',
    'v_limits': [10**(- 5), 10],
    'v_scale': 'log',
    'v_tick_labels': ['$10^{' + str(i * 2 - 4) + '}$' for i in range(3)],
    'v_ticks': [10**(i * 2 - 4) for i in range(3)],
    'v_ticks_minor': [10**(i - 5) for i in range(7)],
    'show_legend': True,
    'legend_location': 'lower right',
    'height': 3.0,
    'width': 6.4,
    'label_font_size': 24,
    'legend_font_size': 20,
    'tick_font_size': 20
})
plotter.update(xs=Ts, vs=G_2_0s)
plotter.get_current_axis().plot(Ts, [1] * len(Ts), '--k')
plotter.show(True)