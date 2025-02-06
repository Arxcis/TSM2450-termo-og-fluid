"""
------------------------------------------------------------------------------
TSM2450:   Oblig 1 Oppg1 - Olje/vann-separator
Student:  Jonas (267431@usn.no)
------------------------------------------------------------------------------
"""

def oppg1():
    rho_vann = 1000 # kg/m3
    rho_olje = 800  # kg/m3
    H_olje = 0.2  # m
    H_vann = 0.8  # m
    g      = 9.81 # m/s**2

    P_atmosfære = 101_000 # Pa
    P_olje      = rho_olje * g * H_olje
    P_vann      = rho_vann * g * H_vann

    P_over = P_olje + P_vann
    P_abs  = P_olje + P_vann + P_atmosfære

    print(f"""
    Oppg1 svar:
          
        P_atmos = {P_atmosfære:>10.1f} Pa 
        P_olje  = {P_olje:>10.1f} Pa
        P_vann  = {P_vann:>10.1f} Pa
        P_over  = {P_over:>10.1f} Pa
        P_abs   = {P_abs:>10.1f} Pa
    """)



if __name__ == "__main__":
    oppg1()
