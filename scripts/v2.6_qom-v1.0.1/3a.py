# dependencies
import numpy as np

# qom modules
from qom.ui.plotters import MPLPlotter

# system parameters
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
data = np.load('data/v2.6_qutip-v4.7.3/3_' + '_'.join([str(param) for param in [N, kappa, gamma, delta_q, delta_2, g_1, Omega, dim_1, dim_2]]) + '.npz')
X = data['arr_0']
Y = data['arr_1']
g_2_0s = data['arr_2']

# track minimum
idx = np.argmin(g_2_0s)
idx_x = idx % dim_1
idx_y = int(idx / dim_1)
pos = (X[idx_y, idx_x], Y[idx_y, idx_x], np.log10(g_2_0s[idx_y, idx_x]))

# plotter
plotter = MPLPlotter(
    axes={
        'X' : X[0],
        'Y' : [y[0] for y in Y]
    },
    params={
        'type'                  : 'contourf',
        'palette'               : 'Reds_r',
        'bins'                  : 21,
        'x_label'               : '$\\delta_{1} / \\kappa$',
        'x_tick_labels'         : ['{:0.2f}'.format(i * 0.05 - 0.1) for i in range(5)],
        'x_tick_position'       : 'bottom-out',
        'x_ticks'               : [i * 0.05 - 0.1 for i in range(5)],
        'x_ticks_minor'         : [i * 0.01 - 0.1 for i in range(21)],
        'y_label'               : '$g_{2} / g_{1}$',
        'y_tick_labels'         : ['{:0.2f}'.format(i * 0.05 + 0.05) for i in range(5)],
        'y_tick_position'       : 'left-out',
        'y_ticks'               : [i * 0.05 + 0.05 for i in range(5)],
        'y_ticks_minor'         : [i * 0.01 + 0.05 for i in range(21)],
        'show_cbar'             : True,
        'cbar_ticks'            : [i * 1 - 4 for i in range(5)],
        'cbar_title'            : '$\\mathrm{log}_{10} [ g^{(2)} (0) ]$',
        'cbar_title_font_dict'  : 'tick',
        'label_font_size'       : 24,
        'tick_font_size'        : 20,
        'width'                 : 6.4,
        'annotations'           : [{
            'text'      : '(a)',
            'xy'        : (0.21, 0.26),
            'font_dict' : 'label',
            'color'     : 'k'
        }, {
            'text'      : '({:0.3f}, {:0.3f})'.format(pos[0], pos[1]),
            'xy'        : (0.51, 0.505),
            # 'xy'        : (0.51, 0.535), # alt
            'font_dict' : 'tick',
            'color'     : 'k'
        }, {
            'text'      : '{:0.2f}'.format(pos[2]),
            'xy'        : (0.51, 0.61),
            # 'xy'        : (0.51, 0.65), # alt
            'font_dict' : 'label',
            'color'     : 'k'
        }]
    }
)
plotter.update(
    vs=np.log10(g_2_0s)
)
fig = plotter.get_current_figure()
ax = fig.axes[0]
ax.plot(X[0], [pos[1]] * len(X[0]), linestyle='--', linewidth=1, color='k')
ax.plot([pos[0]] * len(Y[:, 0]), Y[:, 0], linestyle='--', linewidth=1, color='k')
ax.scatter([pos[0]], [pos[1]], s=100, marker='o', facecolors='none', edgecolors='k')
plotter.show()