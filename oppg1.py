"""
------------------------------------------------------------------------------
TSM2450:   Oblig 1 Oppg1 - Olje/vann-separator
Student:  Jonas (267431@usn.no)
------------------------------------------------------------------------------
"""

def oppg1():

    print("""
    Oppg1:

    Det skal kjøpes en olje/vann-separator lik den i bildet under. Det blå er vann (i bunn) og det beige er olje. Fra nær bunn går det ett rør oppover til å se nivået i tanken.

        a) Dersom oljen har en tetthet på 800 kg/m3 og har en høyde på 20cm, hva er da trykket i bunn av tanken om trykket i gassen i toppen er atmosfærisk?
    """)
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
        Svar:
          P_atmos = {P_atmosfære:>10.1f} Pa 
          P_olje  = {P_olje:>10.1f} Pa
          P_vann  = {P_vann:>10.1f} Pa
          P_over  = {P_over:>10.1f} Pa
          P_abs   = {P_abs:>10.1f} Pa

    """)

    print("""
        b) Dersom oljelaget kan forandre tykkelse, vil da røret for å se nivået fungere? Vis med formler og fysikk. Hint: Det er ikke olje i røret
    """)

    print("""
        Svar: 1 ligning med 2 ukjente -> Dårlig måleprinsipp
          """)



if __name__ == "__main__":
    oppg1()
