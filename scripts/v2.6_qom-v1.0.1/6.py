# dependencies
import numpy as np

# qom modules
from qom.ui.plotters import MPLPlotter

# system parameters
N       = 5
kappa   = 1.0
gamma   = 1.11 * kappa
# gamma   = 1.1 * kappa # alt
delta_2 = 0.1 * kappa
g_1     = 0.8 * kappa
g_2     = 0.1 * kappa
Omega   = 1e-3 * kappa
dim_1   = 101
dim_2   = 501

# load data
data = np.load('data/v2.6_qutip-v4.7.3/6_' + '_'.join([str(param) for param in [N, kappa, gamma, delta_2, g_1, g_2, Omega, dim_1, dim_2]]) + '.npz')
X = data['arr_0']
Y = data['arr_1']
g_2_0s = data['arr_2']

# track minimum
idx_1 = np.argmin(g_2_0s[:int(dim_2 / 2)])
idx_1_x = idx_1 % dim_1
idx_1_y = int(idx_1 / dim_1)
pos_1 = (X[idx_1_y, idx_1_x], Y[idx_1_y, idx_1_x], np.log10(g_2_0s[idx_1_y, idx_1_x]))
idx_2 = np.argmin(g_2_0s[int(dim_2 / 2):])
idx_2_x = idx_2 % dim_1
idx_2_y = int(idx_2 / dim_1) + int(dim_2 / 2)
pos_2 = (X[idx_2_y, idx_2_x], Y[idx_2_y, idx_2_x], np.log10(g_2_0s[idx_2_y, idx_2_x]))

# plotter
plotter = MPLPlotter(
    axes={
        'X' : X[0],
        'Y' : [y[0] for y in Y]
    },
    params={
        'type'                  : 'contourf',
        'palette'               : 'RdBu',
        'bins'                  : 41,
        'x_label'               : '$\\delta_{1} / \\kappa$',
        'x_tick_labels'         : ['{:0.2f}'.format(i * 0.25 - 0.5) for i in range(5)],
        'x_tick_position'       : 'bottom-out',
        'x_ticks'               : [i * 0.25 - 0.5 for i in range(5)],
        'x_ticks_minor'         : [i * 0.05 - 0.5 for i in range(21)],
        'y_label'               : '$\\delta_{q} / \\kappa$',
        'y_tick_labels'         : ['{:0.2f}'.format(i * 0.1 - 0.2) for i in range(5)],
        'y_tick_position'       : 'left-out',
        'y_ticks'               : [i * 0.1 - 0.2 for i in range(5)],
        'y_ticks_minor'         : [i * 0.025 - 0.25 for i in range(21)],
        'show_cbar'             : True,
        'cbar_ticks'            : [i * 1 - 4 for i in range(5)],
        'cbar_title'            : '$\\mathrm{log}_{10} [ g^{(2)} (0) ]$',
        'cbar_title_font_dict'  : 'tick',
        'label_font_size'       : 24,
        'tick_font_size'        : 20,
        'width'                 : 6.4,
        'annotations'           : [{
            'text'      : '({:0.2f}, {:0.3f})'.format(pos_1[0], pos_1[1]),
            'xy'        : (0.428, 0.325),
            # 'xy'        : (0.46, 0.3), # alt
            'font_dict' : 'tick',
            'color'     : 'k'
        }, {
            'text'      : '{:0.2f}'.format(pos_1[2]),
            'xy'        : (0.56, 0.435),
            # 'xy'        : (0.59, 0.395), # alt
            'font_dict' : 'label',
            'color'     : 'k'
        }, {
            'text'      : '({:0.2f}, {:0.3f})'.format(pos_2[0], pos_2[1], pos_2[2]),
            'xy'        : (0.33, 0.73),
            # 'xy'        : (0.3, 0.755), # alt
            'font_dict' : 'tick',
            'color'     : 'k'
        }, {
            'text'      : '{:0.2f}'.format(pos_2[2]),
            'xy'        : (0.33, 0.62),
            # 'xy'        : (0.3, 0.65), # alt
            'font_dict' : 'label',
            'color'     : 'k'
        }]
    }
)
plotter.update(
    vs=np.log10(g_2_0s)
)
ax = plotter.get_current_figure().axes[0]
colors = plotter.get_colors(
    palette='RdBu_r',
    bins=11
)
ax.plot([pos_1[0]] * len(Y[:, 0]), Y[:, 0], linestyle='--', linewidth=1, color=colors[-2])
ax.plot(X[0], [pos_1[1]] * len(X[0]), linestyle='--', linewidth=1, color=colors[1])
ax.scatter([pos_1[0]], [pos_1[1]], s=100, marker='o', facecolors='none', edgecolors='k')
ax.plot([pos_2[0]] * len(Y[:, 0]), Y[:, 0], linestyle='--', linewidth=1, color=colors[1])
ax.plot(X[0], [pos_2[1]] * len(X[0]), linestyle='--', linewidth=1, color=colors[-2])
ax.scatter([pos_2[0]], [pos_2[1]], s=100, marker='o', facecolors='none', edgecolors='k')
plotter.show()