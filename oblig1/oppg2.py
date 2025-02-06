#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------
TSM2450:   Oblig 1 Oppg2 - Ventilasjonsanlegg
Student:  Jonas (267431@usn.no)
------------------------------------------------------------------------------
"""

from dataclasses import dataclass

@dataclass
class Rør:
    """Representerer et rør som skal levere luft til et rom"""
    navn: str       
    areal: float    # m2 - areal til rommet som røret skal levere til
    lengde: float   # m  - lengde til røret

    personer: int  = None #      - antall personer som funksjon av arealet til rommet
    Q: float       = None # m3/s - volumflyt som funksjon av antall personer
    A_min: float   = None # m2   - minste tverrsnitt som funksjon av Q
    A_hylle: float = None # m2   - hylletverrsnitt som funksjon av minste tverrsnitt
    volum: float   = None # m3   - volum som funksjon av lengde og hylletverrsnitt


def main():
    """Regner ut totalverdier til 4 alternativer A, B, C og D og skriver til skjerm"""

    Alternativ_A_trestruktur_inn_fra_vest = [
        Rør(navn="fra hoved til 80", lengde=5.0,  areal=80+160+80+40+80+40+80+70),
        Rør(navn="fra 80 til 160",   lengde=5.0,  areal=160+80+40+80+40+80+70),
        Rør(navn="fra 160 til 80",   lengde=5.0,  areal=80+40+80+40+80+70),
        Rør(navn="fra 80 til 40",    lengde=7.5,  areal=40+80+40+80+70),
        Rør(navn="fra 40 til 80",    lengde=2.5,  areal=80+40+80+70),
        Rør(navn="fra 80 til 40",    lengde=2.5,  areal=40+80+70),
        Rør(navn="fra 40 til 70+80",    lengde=7.5,  areal=80+70),

        Rør(navn="inn 80",           lengde=5.0,  areal=80),
        Rør(navn="inn 160",          lengde=5.0,  areal=160),
        Rør(navn="inn 80",           lengde=5.0,  areal=80),
        Rør(navn="inn 40",           lengde=5.0,  areal=40),
        Rør(navn="inn 80",           lengde=5.0,  areal=80),
        Rør(navn="inn 40",           lengde=5.0,  areal=40),
        Rør(navn="inn 80",           lengde=5.0,  areal=80),
        Rør(navn="inn 70",           lengde=4.5,  areal=70),
    ]

    Alternativ_B_trestruktur_inn_fra_øst = [
        Rør(navn="fra hoved til 70+80", lengde=5.0,  areal=80+160+80+40+80+40+80+70),
        Rør(navn="fra 70+80 til 40",    lengde=7.5,  areal=80+160+80+40+80+40),
        Rør(navn="fra 40 til 80",    lengde=2.5,  areal=80+160+80+40+80),
        Rør(navn="fra 80 til 40",    lengde=2.5,  areal=80+160+80+40),
        Rør(navn="fra 40 til 80",    lengde=7.5,  areal=80+160+80),
        Rør(navn="fra 80 til 160",   lengde=5.0,  areal=80+160),
        Rør(navn="fra 160 til 80",   lengde=5.0,  areal=80),

        Rør(navn="inn 80",           lengde=5.0,  areal=80),
        Rør(navn="inn 160",          lengde=5.0,  areal=160),
        Rør(navn="inn 80",           lengde=5.0,  areal=80),
        Rør(navn="inn 40",           lengde=5.0,  areal=40),
        Rør(navn="inn 80",           lengde=5.0,  areal=80),
        Rør(navn="inn 40",           lengde=5.0,  areal=40),
        Rør(navn="inn 80",           lengde=5.0,  areal=80),
        Rør(navn="inn 70",           lengde=4.5,  areal=70),
    ]

    Alternativ_C_trestruktur_inn_fra_midten = [
        Rør(navn="hoved",      lengde=1.5,  areal=160+80+80+80+80+70+40+40),

        Rør(navn="vestre",     lengde=15.0, areal=160+80+80),
        Rør(navn="vestre 80",  lengde=5.0,  areal=80),
        Rør(navn="vestre 160", lengde=5.0,  areal=160),
        Rør(navn="vestre 80",  lengde=5.0,  areal=80),
        
        Rør(navn="østre",    lengde=15.0, areal=80+80+70+40+40),
        Rør(navn="østre 40", lengde=5.0,  areal=40),
        Rør(navn="østre 80", lengde=5.0,  areal=80),
        Rør(navn="østre 40", lengde=5.0,  areal=40),
        Rør(navn="østre 80", lengde=5.0,  areal=80),
        Rør(navn="østre 70", lengde=4.5,  areal=70),
    ]

    Alternativ_D_gaffel_fra_vest = [
        Rør(navn="inn fra vest", lengde=2.5, areal=160+80+80+80+80+70+40+40),
        
        Rør(navn="Nord",                lengde=12.5,  areal=80+80+160),
        Rør(navn="Nord fra 160 til 80", lengde=15.0,  areal=80+80),
        Rør(navn="Nord fra 80 til 80", lengde=10.0,  areal=80),
        
        Rør(navn="Sør",               lengde=7.5,  areal=70+40+40+80+80),
        Rør(navn="Sør fra 80 til 80", lengde=10.0,  areal=70+40+40+80),
        Rør(navn="Sør fra 80 til 40", lengde=7.5,  areal=70+40+40),
        Rør(navn="Sør fra 40 til 40", lengde=5.0,  areal=70+40),
        Rør(navn="Sør fra 40 til 70", lengde=7.5,  areal=70),
    ]

    A = beregn_total(røra=Alternativ_A_trestruktur_inn_fra_vest)
    B = beregn_total(røra=Alternativ_B_trestruktur_inn_fra_øst)
    C = beregn_total(røra=Alternativ_C_trestruktur_inn_fra_midten)
    D = beregn_total(røra=Alternativ_D_gaffel_fra_vest)

    resultater = [A, B, C, D]

    from pandas import DataFrame
    
    print(DataFrame({
        "Antall rør": (res["antall"] for res in resultater),
        "Rørlengde [m]": (res["lengde"] for res in resultater),
        "Rørvolum [m2]": (res["volum"] for res in resultater),
    }, index=(
        "A: Trestruktur fra vest",
        "B: Trestruktur fra øst",
        "C: Trestruktur fra midten",
        "D: Gaffel fra vest",
    )))

    
def beregn_total(røra):
    """Beregner og returnerer total rørlengde, rørvolum og antall rør"""
    #
    # 1. Innstillinger
    #
    Persontetthet          = 0.7 # person/m2
    Q_luft_pers_per_time   = 26  # m3/t
    V_max                  = 10  # m/s
    Q_luft_pers_per_sekund = Q_luft_pers_per_time / 3600  # m3/pers/s

    #
    # 2. Beregninger
    #    
    from math import ceil

    for rør in røra:
        # 2.1 Regn ut antall personer som røret skal føre luft til.
        rør.personer = ceil(rør.areal * Persontetthet)

        # 2.2 Regn ut Q som røret må ha, for å forsyne antall personer.
        rør.Q = Q_luft_pers_per_sekund * rør.personer
        
        # 2.3. Regn ut minste tverrsnitt som røret må ha for å forsyne Q.
        rør.A_min = rør.Q / V_max
        
        # 2.4. Velg hyllevare som er nærmest minste tverrsnitt.
        A_hylle, error = velg_hyllevare(rør.A_min)
        if error:
            print(f"Feil med {rør.navn}: ", error)
            exit(1)

        rør.A_hylle = A_hylle
        
        # 2.5. Regn ut rørvolum som rørlengde * hylletverrsnitt.
        rør.volum = rør.A_hylle * rør.lengde
    
    lengde = sum([rør.lengde for rør in røra])             # m
    volum  = sum([rør.lengde*rør.A_hylle for rør in røra]) # m3
    antall = len(røra)

    total = {
        "lengde": lengde,
        "volum": volum,
        "antall": antall,
    }

    return total

def velg_hyllevare(A_min: float):
    """
    A_min: float - minsteverdi for ønske av rør. Velger tilsvarende rør eller nærmeste rør som er større enn denne verdien.
    """
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

    for A_hylle in sorted(HYLLE):
        if A_min < A_hylle:
            return A_hylle, None

    return None, f"Fant ingen varer som har stort nok tverrsnitt til: {A_min} m2"


if __name__ == "__main__":
    main()