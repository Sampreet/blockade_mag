# dependencies
import numpy as np
import os
import sys

# qom modules
from qom.ui.plotters import MPLPlotter
from qom.utils.loopers import run_loopers_in_parallel, wrap_looper

# add path to local libraries
sys.path.append(os.path.abspath(os.path.join('.')))
# import function
from common.g_2_0 import *

# system parameters
N       = 5
kappa   = 1.0
gamma   = 1.11 * kappa
g_1     = 0.8 * kappa
Omega   = 1e-3 * kappa
dim_1   = 1001
dim_2   = 251
dim_3   = 251
load    = True

# function to obtain the blockade condition
def func(system_params):
    delta_q = system_params['delta_q']
    delta_1 = system_params['delta_1']
    delta_2 = delta_q
    g_2 = system_params['g_2']
    return get_condition([kappa, gamma, delta_q, delta_1, delta_2, g_1, g_2, Omega])

if __name__ == '__main__':
    # looper
    looper = run_loopers_in_parallel(
        looper_name='XYZLooper',
        func=func,
        params={
            'show_progress'     : True,
            'file_path_prefix'  : 'data/v2.6_qom-v1.0.1/5',
            'X'                 : {
                'var'   : 'delta_1',
                'min'   : -kappa,
                'max'   : 0.0,
                'dim'   : dim_1
            },
            'Y'                 : {
                'var'   : 'g_2',
                'min'   : 0.05 * g_1,
                'max'   : 0.30 * g_1,
                'dim'   : dim_2
            },
            'Z'                 : {
                'var'   : 'delta_q',
                'min'   : 0.0,
                'max'   : 0.25 * kappa,
                'dim'   : dim_3
            }
        },
        params_system={}
    )
    delta_1s = looper.axes['X']['val']
    g_2s = looper.axes['Y']['val']
    delta_qs = looper.axes['Z']['val']
    conditions = looper.results['V']

    # find positions
    vs = list()
    for i in range(dim_3):
        vs_temp = list()
        for j in range(dim_2):
            vs_temp.append(delta_1s[np.argmin(conditions[i][j])])
        vs.append(vs_temp)

    # plotter
    plotter = MPLPlotter(
        axes={
            'X' : g_2s / g_1, 
            'Y' : delta_qs[::100]
        }, params={
            'type'              : 'lines',
            'palette'           : 'RdBu',
            'bins'              : 41,
            'colors'            : ['k', -1, 0],
            'x_label'           : '$g_{2} / g_{1}$',
            'x_tick_labels'     : ['{:0.2f}'.format(i * 0.05 + 0.05) for i in range(6)],
            # 'x_tick_position'   : 'bottom-out',
            'x_ticks'           : [i * 0.05 + 0.05 for i in range(6)],
            'x_ticks_minor'     : [i * 0.01 + 0.05 for i in range(26)],
            # 'y_label'           : '$\\delta_{q} / \\kappa$, $\\delta_{2} / \\kappa$',
            # 'y_tick_labels'     : ['{:0.2f}'.format(i * 0.05) for i in range(6)],
            # 'y_tick_position'   : 'left-out',
            # 'y_ticks'           : [i * 0.05 for i in range(6)],
            # 'y_ticks_minor'     : [i * 0.01 for i in range(26)],
            # 'show_cbar'         : True,
            # 'cbar_title'        : '$\\delta_{1} / \\kappa$',
            # 'cbar_tick_labels'  : [f'{i * 0.1 - 0.7:0.1f}' for i in range(8)],
            # 'cbar_ticks'        : [i * 0.1 - 0.7 for i in range(8)],
            'v_label'           : '$\\delta_{1_{\\mathrm{opt}}} / \\kappa$',
            'v_limits'          : [-0.7, 0.3],
            'v_tick_labels'     : [f'{i * 0.4 - 0.6:0.1f}' for i in range(3)],
            'v_ticks'           : [i * 0.4 - 0.6 for i in range(3)],
            'v_ticks_minor'     : [i * 0.1 - 0.7 for i in range(9)],
            'show_legend'       : True,
            'legend_labels'     : ['$\\delta_{q} / \\kappa =$ ' + f'{y:0.1f}' for y in [0.0, 0.1, 0.2]],
            'legend_location'   : 'lower right',
            'label_font_size'   : 24,
            'legend_font_size'  : 20,
            'tick_font_size'    : 20,
            'width'             : 6.4,
            'height'            : 3.0
        }
    )
    plotter.update(
        vs=vs[::100],
        xs=g_2s / g_1
    )
    plotter.show()