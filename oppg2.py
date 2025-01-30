
def oppg2():
    """
    TSM2450 Fluidmekanikk Oblig 1
    Oppgave 2
    
    Studentnr: 267431@usn.no 
    """
    #
    # 1. Configure
    #
    areal = int(160 + 4*80 + 2*40 + 70) # m2
    personer_per_areal   = 0.7          # person/m2
    Q_luft_pers_per_time = 26           # m3/t
    v_max                = 10           # m/s
    rør = [
        ("hoved",  160+80+80+80+80+70+40+40),
        ("vestre", 160+80+80),
        ("vestre 160", 160),
        ("vestre 80", 80),
        ("vestre 80", 80),
        
        ("østre", 80+80+70+40+40),
        ("østre 80", 80),
        ("østre 80", 80),
        ("østre 80", 70),
        ("østre 40", 40),
    ]

    #
    # 2. Compute
    #
    personer     = areal * personer_per_areal
    personer_160 = 160 * personer_per_areal
    personer_80  = 80 * personer_per_areal
    personer_70  = 70 * personer_per_areal
    personer_40  = 40 * personer_per_areal 
    personer_vestre = personer_160 + 2*personer_80
    personer_østre  = 2*personer_80 + 2*personer_40 + personer_70

    Q_luft_pers_per_sekund = Q_luft_pers_per_time / 3600  # m3/pers/s
    
    def beregn_rør(navn: str, areal:int):
        personer = areal * personer_per_areal
        Q = Q_luft_pers_per_sekund * personer

        A_min = Q / v_max
        A_hylle, err = velg_hyllerør(A_min)
        if err:
            print(f"Feil med {navn}: ", err)
            exit(1)

        return {
            "navn": navn,
            "Q": round(Q, 3),
            "areal": areal,
            "A_min": round(A_min,3),
            "A_hylle": round(A_hylle, 3),
            "v_max": round(Q / A_min, 1),
            "v_hylle": round(Q / A_hylle, 3),
        } 

    rør = [ beregn_rør(*r) for r in rør]
    
    #
    # 3. Pretty print
    #
    from pandas import DataFrame
    from math import ceil

    print(f"""
Oppg2 svar:

    Innstillinger:
            areal              = {areal} m2

            personer_per_areal = {personer_per_areal} stk
            personer {areal}m2     = {ceil(personer)} stk
            personer 160m2     = {ceil(personer_160)} stk 
            personer  80m2     = {ceil(personer_80)} stk
            personer  70m2     = {ceil(personer_70)} stk 
            personer  40m2     = {ceil(personer_40)} stk

            Q luft per time  = {Q_luft_pers_per_time:>6.1f} m3/person/t
            Q luft per pers  = {Q_luft_pers_per_sekund:>6.4f} m3/person/s

            v_max = {v_max} m/s

    Rør:""")

    print(DataFrame({
        "Rom [m2]": (r["areal"] for r in rør),
        "Q [m3/s]": (r["Q"] for r in rør),
        "A min [m2]": (r["A_min"] for r in rør),
        "A hylle [m2]": (r["A_hylle"] for r in rør),
        "v max [m/s]": (r["v_max"] for r in rør),
        "v hylle [m/s]": (r["v_hylle"] for r in rør),

        }, index=(r["navn"] for r in rør)))
       

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
    oppg2()


