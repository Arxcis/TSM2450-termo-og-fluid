#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TSM2450 Oblig 1
Oppgave: 2
Studentnr: 267431@usn.no 
"""

from dataclasses import dataclass

@dataclass
class Rør:
    """Representerer et rør som skal levere luft til et rom"""
    # Verdier som gis
    navn: str       
    areal: float    # m2 - areal til rommet som røret skal levere til
    lengde: float   # m  - lengde til røret

    # Verdier som skal beregnes
    personer: int  = None #      - antall personer gitt av arealet til rommet
    Q: float       = None # m3/s - volumflyt gitt av antall personer
    A_min: float   = None # m2   - minste tverrsnitt gitt av Q
    A_hylle: float = None # m2   - hylletverrsnitt gitt av minste tverrsnitt
    v_hylle: float = None # m/s  - fart gitt av hylletverrsnitt  
    volum: float   = None # m3   - volum gitt av lengde og hylletverrsnitt


def oppg2():
    """Stiller inn rør, beregner alle verdier og skriver til skjerm"""
    #
    # 1. Innstillinger
    #
    Persontetthet   = 0.7 # person/m2
    Q_luft_pers_per_time = 26  # m3/t
    V_max                = 10  # m/s

    Røra = [
        Rør(navn="hoved",      lengde=1.5,  areal=160+80+80+80+80+70+40+40),

        Rør(navn="vestre",     lengde=15.0, areal=160+80+80),
        Rør(navn="vestre 160", lengde=5.0,  areal=160),
        Rør(navn="vestre 80",  lengde=5.0,  areal=80),
        Rør(navn="vestre 80",  lengde=5.0,  areal=80),
        
        Rør(navn="østre",    lengde=15.0, areal=80+80+70+40+40),
        Rør(navn="østre 80", lengde=5.0,  areal=80),
        Rør(navn="østre 80", lengde=5.0,  areal=80),
        Rør(navn="østre 70", lengde=4.5,  areal=70),
        Rør(navn="østre 40", lengde=5.0,  areal=40),
    ]

    #
    # 2. Beregninger
    #
    Q_luft_pers_per_sekund = Q_luft_pers_per_time / 3600  # m3/pers/s
    
    from math import ceil

    for rør in Røra:
        rør.personer = ceil(rør.areal * Persontetthet)
        rør.Q = Q_luft_pers_per_sekund * rør.personer
        rør.A_min = rør.Q / V_max
        
        A_hylle, err = velg_hylletverrsnitt(rør.A_min)
        if err:
            print(f"Feil med {rør.navn}: ", err)
            exit(1)

        rør.A_hylle = A_hylle
        rør.v_hylle = rør.Q / rør.A_hylle
        rør.volum = rør.A_hylle * rør.lengde

    areal = Røra[0].areal
    personer = Røra[0].personer
    lengde = sum([rør.lengde for rør in Røra])             # m
    volum  = sum([rør.lengde*rør.A_hylle for rør in Røra]) # m3


    #
    # 3. Pretty print
    #
    from pandas import DataFrame
    import textwrap

    print(f"""
#
# Oppg2 svar:
#

    Innstillinger:
        V max           = {V_max:>8.1f} m/s
        Q luft per time = {Q_luft_pers_per_time:>8.1f} m3/person/t
        Persontetthet   = {Persontetthet:>8.1f} person/m2
        """)

    print(textwrap.indent(DataFrame({
            "Lengde [m]": (rør.lengde for rør in Røra),
            "Areal [m2]": (rør.areal for rør in Røra),
        }, index=(rør.navn for rør in Røra)).to_string(), "        "))
    

    print(f"""
    Beregninger:
        Q luft per sekund = {Q_luft_pers_per_sekund:.4f} m3/person/s

        Total personer  = {ceil(personer):>6} stk
        Total romareal  = {areal:>6.2f} m2
        Total rørlengde = {lengde:>6.2f} m
        Total rørvolum  = {volum:>6.2f} m3
          """)
    
    print(textwrap.indent(DataFrame({
            "Personer": (rør.personer for rør in Røra),
            "Q [m3/s]": (round(rør.Q, 3) for rør in Røra),
            "A min [m2]": (round(rør.A_min, 3) for rør in Røra),
            "A hylle [m2]": (round(rør.A_hylle, 3) for rør in Røra),
            "len [m]": (round(rør.lengde, 3) for rør in Røra),
            "volum [m3]": (round(rør.volum, 3) for rør in Røra),
            "v hylle [m/s]": (round(rør.v_hylle, 3) for rør in Røra),
        }, index=(rør.navn for rør in Røra)).to_string(), "        "))
    

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

def velg_hylletverrsnitt(A_min: float):
    """
    A_min: float - minsteverdi for ønske av rør. Velger tilsvarende rør eller nærmeste rør som er større enn denne verdien.
    """

    for i, A_hylle in enumerate(sorted(HYLLE)):
        if A_min < A_hylle:
            return A_hylle, None

    return None, f"Fant ingen varer som har stort nok tverrsnitt til: {A_min} m2"


if __name__ == "__main__":
    oppg2()
