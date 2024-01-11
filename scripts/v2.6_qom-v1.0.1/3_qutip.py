# dependencies
import numpy as np
import qutip
import time

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

# operators
s_q = qutip.tensor(qutip.destroy(2), qutip.qeye(N), qutip.qeye(N))
m_1 = qutip.tensor(qutip.qeye(2), qutip.destroy(N), qutip.qeye(N))
m_2 = qutip.tensor(qutip.qeye(2), qutip.qeye(N), qutip.destroy(N))
n_q = s_q.dag() * s_q
n_1 = m_1.dag() * m_1
n_2 = m_2.dag() * m_2
num = m_1.dag() * m_1.dag() * m_1 * m_1

# initialize
delta_1s = np.linspace(-0.1, 0.1, dim_1) * kappa
g_2s = np.linspace(0.05, 0.25, dim_2) * g_1
X, Y = np.meshgrid(delta_1s / kappa, g_2s / g_1)
g_2_0s = np.zeros((dim_2, dim_1))
start = time.time()

# collapse operators
c_ops = [np.sqrt(kappa) * m_1, np.sqrt(kappa) * m_2, np.sqrt(gamma) * s_q]

# iterate
for i in range(len(g_2s)):
    # display
    time_elapsed = time.time() - start
    progress = i / (dim_2 - 1) * 100
    print('\r{:0.3f}s\t'.format(time_elapsed) + ('\t' if time_elapsed < 100.0 else '') + 'Progress: {:0.2f}%'.format(progress), end='\t')

    # update coupling strength
    g_2 = g_2s[i]
    for j in range(len(delta_1s)):
        # update magnon detuning
        delta_1 = delta_1s[j]

        # Hamiltonian
        H = delta_q * n_q + delta_1 * n_1 + delta_2 * n_2 + g_1 * (s_q.dag() * m_1 + s_q * m_1.dag()) + g_2 * (s_q.dag() * m_2 + s_q * m_2.dag()) + Omega * (m_1.dag() + m_1)

        # steady state sovler
        rho = qutip.steadystate(H, c_ops)

        # update correlations
        g_2_0s[i][j] = qutip.expect(num, rho) / qutip.expect(n_1, rho)**2

# save data
np.savez_compressed('data/v2.6_qom-v1.0.1/3_' + '_'.join([str(param) for param in [N, kappa, gamma, delta_q, delta_2, g_1, Omega, dim_1, dim_2]]), X, Y, g_2_0s)