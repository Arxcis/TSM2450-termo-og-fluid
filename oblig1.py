
def main():
    #
    # TSM2450 Fluidmekanikk Oblig 1
    # Oppgave 1
    #
    # Studentnr: 267431@usn.no
    #

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


    print("""
    Oppg2:

    Det skal kjøpes et nytt ventilasjonsanlegg til klasserommene i Figur 2, og dette må beregnes. Alternativene for rørtykkelser er i tabellen i Figur 3.

          """)

    from math import ceil

    areal = int(160 + 4*80 + 2*40 + 70)
    personer_per_areal = 0.7 # person/m2

    personer     = areal * personer_per_areal
    personer_160 = 160 * personer_per_areal
    personer_80  = 80 * personer_per_areal
    personer_70  = 70 * personer_per_areal
    personer_40  = 40 * personer_per_areal 
    personer_vestre = personer_160 + 2*personer_80
    personer_østre  = 2*personer_80 + 2*personer_40 + personer_70

    # Q for hovedinntak
    Q_luft_pers_per_time = 26                             # m3/t
    Q_luft_pers_per_sekund = Q_luft_pers_per_time / 3600  # m3/pers/s
    Q_luft_hoved  = Q_luft_pers_per_sekund * personer           # m3/s
    
    # Q for vestre fløy
    Q_luft_vestre     = Q_luft_hoved * (personer_vestre / personer)      # m3/s 
    Q_luft_vestre_160 = Q_luft_vestre * (personer_160 / personer_vestre) # m3/s
    Q_luft_vestre_80  = Q_luft_vestre * (personer_80 / personer_vestre)  # m3/s

    # Q for østre fløy
    Q_luft_østre    = Q_luft_hoved - Q_luft_vestre                  # m3/s
    Q_luft_østre_80 = Q_luft_østre * (personer_80 / personer_østre) # m3/s
    Q_luft_østre_40 = Q_luft_østre * (personer_40 / personer_østre) # m3/s
    Q_luft_østre_70 = Q_luft_østre * (personer_70 / personer_østre) # m3/s

    v_max   = int(input("v_max [m/s]: "))                      # m/s

    def lag_rør(navn: str, Q:float):
        return {
            "navn": navn,
            "Q": Q,
            "A": None
        } 

    rør = [
        lag_rør("hoved", Q_luft_hoved),
        lag_rør("vestre", Q_luft_vestre),
        lag_rør("vestre 160m2", Q_luft_vestre_160),
        lag_rør("vestre  80m2", Q_luft_vestre_80),
        lag_rør("vestre  80m2", Q_luft_vestre_80),
        
        lag_rør("østre", Q_luft_østre),
        lag_rør("østre   80m2", Q_luft_østre_80),
        lag_rør("østre   70m2", Q_luft_østre_70),
        lag_rør("østre   40m2", Q_luft_østre_40),
    ]
    
    for r in rør:
        A_min = r["Q"] / v_max # m2 
        A_hylle, err = velg_hyllerør(A_min)
        if err:
            print(f"Feil rør {navn}: ", err)
            exit(1)
        
        r["A_min"]   = A_min
        r["A_hylle"] = A_hylle
        r["v_min"] = r["Q"] / A_min
        r["v_hylle"] = r["Q"] / A_hylle 

       
    #
    # Pretty print the whole shebang
    #
    print(f"""
        svar:
            areal          = {areal} m2
            personer       = {ceil(personer)} stk
            personer 160m2 = {ceil(personer_160)} stk 
            personer  80m2 = {ceil(personer_80)} stk
            personer  70m2 = {ceil(personer_70)} stk 
            personer  40m2 = {ceil(personer_40)} stk

            Q luft per time  = {Q_luft_pers_per_time:>6.1f} m3/person/t
            Q luft per pers  = {Q_luft_pers_per_sekund:>6.4f} m3/person/s

            """ + "\n            ".join([ 
                 f"Q luft {r['navn']:<13}"+" = "+f"{r['Q']:>6.2f} m3/s" for r in rør
            ])+ f"""
            
            v max       = {v_max:>6.2f} m/s
            """ + "".join([f"\n            A min {r['navn']:<13} = {r['A_min']:>6.3f} m2" for r in rør])
            + "\n"+
          "".join([f"\n            A hylle {r['navn']:<13} = {r['A_hylle']:>6.3f} m2" for r in rør]) 

  + "\n"+
          "".join([f"\n            v min {r['navn']:<13} = {r['v_min']:>6.3f} m/s" for r in rør]) + "\n" +
          "".join([f"\n            v hylle {r['navn']:<13} = {r['v_hylle']:>6.3f} m/s" for r in rør]) 
          + "\n" 
          )



# Velg hovedrør automatisk basert på A_hoved
HYLLE = [
    0.003, # m2
    0.005,
    0.008,
    0.012,
    0.020,
    0.031,
    0.049,
    0.078,
    0.126,
    0.196,
    0.312,
    0.503,
    0.785,
    1.227,
    2.011,
]    
def velg_hyllerør(A_min: float):
    """
    A_min: float - minsteverdi for ønske av rør. Velger tilsvarende rør eller nærmeste rør som er større enn denne verdien.
    """

    for i, A_hylle in enumerate(sorted(HYLLE)):
        if A_min < A_hylle:
            return A_hylle, None

    return None, f"Fant ingen varer som har stort nok tverrsnitt til: {A_min} m2"


if __name__ == "__main__":
    main()
