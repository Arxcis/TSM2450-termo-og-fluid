"""
------------------------------------------------------------------------------
TSM2450:   Oblig 2 Oppg1 - 3 dyser og 1 pumpe
Student:  Jonas (267431@usn.no)
------------------------------------------------------------------------------
"""

from math import pi
from numpy import array, ndarray, append

# Globale konstanter
ρ_vanntetthet = 1000
μ_vannviskositet = 0.001
g = 9.81
LITER_M3 = 1000
SEKUND_MINUTT = 60
PASCAL_BAR = 1e5
PASCAL_METER = (ρ_vanntetthet*g)
METER_PASCAL = PASCAL_METER**-1
BAR_METER = PASCAL_METER/PASCAL_BAR


def main():
    """Regner ut hvilket trykk, volumstrøm og effekt en pumpe må ha for ulike dyser og en gitt statisk dysetrykk."""

    # Innstillinger
    Δhp_statiskbar = 7.0
    Δhp_statiskpascal = Δhp_statiskbar * 100_000
    Δhp_statiskmeter  = Δhp_statiskpascal * METER_PASCAL
    dysefaktor = array([17, 56, 107])

    # Beregninger
    volumstrøm = finn_dysestrøm(dysefaktor, Δhp_statiskbar) # 3 dyser i Oppg1a)
    volumstrøm = append(volumstrøm, 5e-3)                   # 1 pumpe i oppg1b)
    pumpemeter = finn_pumpemeter(volumstrøm, Δhp_statiskmeter)
    effekt     = finn_pumpeeffekt(volumstrøm, pumpemeter)

    # Resultat
    print("dysefaktor: ", dysefaktor, "")
    print("volumstrøm: ", volumstrøm, "[m3/sekund]")
    print("volumstrøm: ", volumstrøm*LITER_M3*SEKUND_MINUTT, "[l/min]")
    print("pumpetrykk: ", pumpemeter*BAR_METER, "[Bar]")
    print("effekt: ", effekt, "[Watt]")


def finn_dysestrøm(dysefaktor: float | ndarray, Δhp_statiskbar: float):
    """Finner volumstrømmen i kubikkmeter/sekund, for en gitt dysefaktor og ønsket statisk trykkøkning i bar"""

    Q_volumstrømliter_min = dysefaktor * (Δhp_statiskbar)**0.5
    Q_volumstrøm = Q_volumstrømliter_min / (LITER_M3 * SEKUND_MINUTT)

    return Q_volumstrøm


def finn_pumpemeter(Q_volumstrøm: float | ndarray, Δhp_statiskmeter: float):
    """Finner pumpetrykket i meter, for en gitt volumstrøm og ønsket statisk trykkøkning i meter"""

    # Innstillinger
    antall_albuer = 4
    ε_ruhetmeter  = 0.0005
    D_rørdiameter = 0.050
    ΔZ_høydemeter = 13.0
    K_albue       = 0.9  # K-faktor for "90 degree elbow" fra diagram 10.2 i boka
    K_sete        = 10.0 # K-faktor for "Globe valve" fra diagram 10.2 i boka
    L_rørlengdemeter = 50

    A_rørtverrsnitt = (pi/4)*D_rørdiameter**2
    v_fluidmeter_sekund = Q_volumstrøm / A_rørtverrsnitt

    f_rør = f_rørfriksjonskoeffisent(
        ρ=ρ_vanntetthet,
        μ=μ_vannviskositet,
        v=v_fluidmeter_sekund,
        d=D_rørdiameter,
        ε=ε_ruhetmeter,
    )

    Δhdyn_dynamiskmeter = (v_fluidmeter_sekund**2/(2*g)) - 0 # <- Antar ~ 0m/s ved toppen av tanken.
    hf_rørtapmeter      = f_rør   * Δhdyn_dynamiskmeter * (L_rørlengdemeter/D_rørdiameter) 
    h0_albuetapmeter    = K_albue * Δhdyn_dynamiskmeter
    h0_setetapmeter     = K_sete  * Δhdyn_dynamiskmeter
  
    # Bernouli 
    hp_pumpemeter = ΔZ_høydemeter\
                  + Δhp_statiskmeter\
                  + Δhdyn_dynamiskmeter\
                  + hf_rørtapmeter\
                  + h0_setetapmeter\
                  + h0_albuetapmeter * antall_albuer

    return hp_pumpemeter


def finn_pumpeeffekt(Q_volumstrøm: float | ndarray, hp_pumpemeter: float | ndarray):
    """Finner effekt til pumpe - P = rho*q*Q*hp - i Watt"""

    return ρ_vanntetthet * g * Q_volumstrøm * hp_pumpemeter


def f_rørfriksjonskoeffisent(v: float | ndarray, ρ: float, d: float, μ: float, ε: float):
    """Gir en tilnærming til Moodys diagram for turbulent strømning Re > 4000"""
    from numpy import log10

    Re = (ρ*v*d)/μ

    A = 1/(3.7*(d/ε))
    B = 5.74/(Re**0.9)

    return 0.25 / (log10(A+B)**2)


if __name__ == "__main__":
    main()
