import numpy as np
import qutip
import scipy.constants as sc
import time

# parameters
N       = 5
kappa   = 1.0
gamma   = 1.11 * kappa
g_1     = 0.8 * kappa
Omega   = 1e-3 * kappa
omega_ms= [8.2e9, 8.6e9]
dim     = 201

# zero detunings
delta_q = 0.0 * kappa
delta_1 = 0.0 * kappa
delta_2 = 0.0 * kappa
g_2     = 0.161 * g_1

# # finite detunings
# delta_q = 0.1 * kappa
# delta_1 = -0.276 * kappa
# delta_2 = 0.1 * kappa
# g_2     = 0.137 * g_1

# operators
s_q = qutip.tensor(qutip.destroy(2), qutip.qeye(N), qutip.qeye(N))
m_1 = qutip.tensor(qutip.qeye(2), qutip.destroy(N), qutip.qeye(N))
m_2 = qutip.tensor(qutip.qeye(2), qutip.qeye(N), qutip.destroy(N))
n_q = s_q.dag() * s_q
n_1 = m_1.dag() * m_1
n_2 = m_2.dag() * m_2
num = m_1.dag() * m_1.dag() * m_1 * m_1

# Hamiltonian
H = delta_q * n_q + delta_1 * n_1 + delta_2 * n_2 + g_1 * (s_q.dag() * m_1 + s_q * m_1.dag()) + g_2 * (s_q.dag() * m_2 + s_q * m_2.dag()) + Omega * (m_1.dag() + m_1)

# initialize
Ts      = np.linspace(2, 6, dim) * 1e-3
g_2_0s  = np.zeros(dim)
start   = time.time()

# iterate
for i in range(len(Ts)):
    # display
    time_elapsed = time.time() - start
    progress = i / (dim - 1) * 100
    print('\r{:0.3f}s\t'.format(time_elapsed) + ('\t' if time_elapsed < 100.0 else '') + 'Progress: {:0.2f}%'.format(progress), end='\t')

    n_ths = [1 / (np.exp(sc.hbar * omega / sc.k / Ts[i]) - 1) for omega in omega_ms]
    # print(Ts[i], n_ths)

    # update values
    c_ops = [
        np.sqrt(kappa * (n_ths[0] + 1)) * m_1,
        np.sqrt(kappa * n_ths[0]) * m_1.dag(),
        np.sqrt(kappa * (n_ths[1] + 1)) * m_2,
        np.sqrt(kappa * n_ths[1]) * m_2.dag(),
        np.sqrt(gamma) * s_q
    ]

    # steady state sovler
    rho = qutip.steadystate(H, c_ops)

    # update correlations
    g_2_0s[i] = qutip.expect(num, rho) / qutip.expect(n_1, rho)**2

# save data
np.savez_compressed('data/figs/7_' + '_'.join([str(param) for param in [N, kappa, gamma, delta_q, delta_1, delta_2, g_1, g_2, Omega, dim]]), Ts, g_2_0s)