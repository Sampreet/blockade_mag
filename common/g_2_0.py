import numpy as np

def get_g_2_0_analytical(params):
    kappa, gamma, delta_q, delta_1, delta_2, g_1, g_2, Omega = params
        
    # frequently used expressions
    Delta_q = delta_q - 1j * gamma / 2
    Delta_1 = delta_1 - 1j * kappa / 2
    Delta_2 = delta_2 - 1j * kappa / 2
    Delta_2_prime = Delta_2 + Delta_q - g_2**2 / Delta_2
    Delta_1_prime = Delta_1 + Delta_2 - g_1**2 / Delta_2_prime

    alpha = Delta_1_prime * Delta_2 / g_2 / Omega - Omega / g_2
    beta = alpha * (Delta_1 + Delta_q) - Delta_2 * g_2 / Omega
    Gamma = Omega + Delta_1_prime * (Delta_1 + Delta_q) / Omega - g_2**2 / Omega

    eta_1 = np.sqrt(2) * (Omega - g_1**2 / Gamma)
    eta_2 = np.sqrt(2) * g_1 * (Delta_q + Delta_1_prime) / Gamma
    eta_3 = np.sqrt(2) * (Delta_1 - g_1**2 * Delta_1_prime / Omega / Gamma)

    theta_1 = g_1 * beta / Gamma
    theta_2 = Omega * alpha + g_2 - beta * (Delta_q + Delta_1_prime) / Gamma
    theta_3 = g_1 * (alpha - Delta_1_prime * beta / Omega / Gamma)

    # numerator and denominator
    num_1_temp = Omega * (g_1 * theta_3 - Omega * theta_2)
    num_1 = abs(num_1_temp)**2

    num_2_temp = (Omega * eta_1 - Delta_1 * eta_3) * theta_2 - eta_2 * (Omega * theta_1 + Delta_1 * theta_3) - g_1 * (eta_3 * theta_1 + eta_1 * theta_3)
    num_2 = abs(num_2_temp)**2

    den_temp = Omega * (eta_3 * theta_2 + eta_2 * theta_3)
    den = abs(den_temp)**4

    # amplitude probabilities
    C_20g = Omega * (- Omega * theta_2 + g_1 * theta_3) / ((Omega * eta_1 - Delta_1 * eta_3) * theta_2 - eta_2 * (Omega * theta_1 + Delta_1 * theta_3) - g_1 * (eta_3 * theta_1 + eta_1 * theta_3))

    C_10g = Omega * (eta_3 * theta_2 + eta_2 * theta_3) / ((Omega * eta_1 - Delta_1 * eta_3) * theta_2 - eta_2 * (Omega * theta_1 + Delta_1 * theta_3) - g_1 * (eta_3 * theta_1 + eta_1 * theta_3))
    
    # # zero time correlation
    # g_2_0 = np.real(2 * num_1 * num_2 / den)
    g_2_0 = np.real(2 * abs(C_20g)**2 / abs(C_10g)**4)

    return g_2_0

def get_g_2_0_simplified(params):
    kappa, gamma, delta_q, delta_1, delta_2, g_1, g_2, Omega = params
        
    # frequently used expressions
    Delta_1 = delta_1 - 1j * kappa / 2
    Delta_2 = delta_2 - 1j * kappa / 2
    Delta_q = delta_q - 1j * gamma / 2
    Delta_2_prime = Delta_2 + Delta_q - g_2**2 / Delta_2
    Delta_1_tilde = Delta_q + Omega**2 / Delta_1 - g_1**2 / Delta_1
    Delta_2_tilde = Delta_q + Omega**2 / Delta_2 - g_2**2 / Delta_2
    Delta_s = Delta_1 + Delta_2 + Delta_q

    # first expression
    A_0 = Omega * Delta_2 * Delta_2_tilde
    A_1 = Delta_1 * Delta_2 * Delta_2_tilde + Omega**2 * Delta_s - g_1**2 * Delta_2
    A_2 = np.sqrt(2) * Omega * (Delta_1 * Delta_s + Delta_2 * Delta_2_tilde - g_1**2)

    # second expression
    B_0 = Omega**2 * (Delta_2_prime * Delta_s - g_1**2)
    B_1 = Omega * (2 * Delta_1 * (Delta_2_prime * Delta_s - g_1**2) + (Delta_2 * Delta_2_tilde - g_1**2) * Delta_2_prime - g_1**2 * Delta_q)
    B_2 = np.sqrt(2) * ((Delta_2_prime * (Delta_1 + Delta_2) - g_1**2) * (Delta_1 * Delta_1_tilde + Delta_1**2) - g_2**2 * Delta_1 * Delta_2_prime + Omega**2 * Delta_2_prime * (Delta_1 + Delta_q))

    # amplitude probabilities
    C_10g = (A_2 * B_0 - A_0 * B_2) / (A_1 * B_2 - A_2 * B_1)
    C_20g = (A_0 * B_1 - A_1 * B_0) / (A_1 * B_2 - A_2 * B_1)

    # zero time correlation
    # g_2_0 = 2 * abs(A_0 * B_1 - A_1 * B_0)**2 * abs(A_1 * B_2 - A_2 * B_1)**2 / abs(A_2 * B_0 - A_0 * B_2)**4
    g_2_0 = 2 * abs(C_20g)**2 / abs(C_10g)**4

    return g_2_0

def get_condition(params):
    kappa, gamma, delta_q, delta_1, delta_2, g_1, g_2, Omega = params
        
    # frequently used expressions
    Delta_1 = delta_1 - 1j * kappa / 2
    Delta_2 = delta_2 - 1j * kappa / 2
    Delta_q = delta_q - 1j * gamma / 2
    Delta_2_prime = Delta_2 + Delta_q - g_2**2 / Delta_2
    Delta_2_tilde = Delta_q + Omega**2 / Delta_2 - g_2**2 / Delta_2
    Delta_s = Delta_1 + Delta_2 + Delta_q

    # first expression
    A_0 = Omega * Delta_2 * Delta_2_tilde
    A_1 = Delta_1 * Delta_2 * Delta_2_tilde + Omega**2 * Delta_s - g_1**2 * Delta_2

    # second expression
    B_0 = Omega**2 * (Delta_2_prime * Delta_s - g_1**2)
    B_1 = Omega * (2 * Delta_1 * (Delta_2_prime * Delta_s - g_1**2) + (Delta_2 * Delta_2_tilde - g_1**2) * Delta_2_prime - g_1**2 * Delta_q)

    return abs(A_0 * B_1 - A_1 * B_0)
