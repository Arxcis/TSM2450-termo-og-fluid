
from math import pi

# Konstanter
ρ_vanntetthet = 1000
μ_vannviskositet = 0.001
g = 9.81
LITER_M3 = 1000
SEKUND_MINUTT = 60


def main():
    # 3 dyser gir 3 ulike pumpetrykk 
    hp17_pumpetrykk = finn_pumpetrykk(17)
    hp56_pumpetrykk = finn_pumpetrykk(56)
    hp107_pumpetrykk = finn_pumpetrykk(107)
    

def finn_pumpetrykk(dysefaktor):
    """Finner pumpetrykket i meter, for en gitt dysefaktor"""

    # Innstillinger
    antall_albuer = 4
    ε_ruhetmeter  = 0.001
    D_rørdiameter = 0.050
    ΔZ_høydemeter = 13.0
    L_rørlengdemeter = 50
    Δhp_statisktrykk = (7.0e6 - 0) # <- Antar 0Pa overtrykk ved innløpet/toppen av tanken.
   
    # Beregninger
    Q_volumstrøm_liter_min = dysefaktor * (Δhp_statisktrykk)**0.5
    Q_volumstrøm_m3_sekund = Q_volumstrøm_liter_min / (LITER_M3 * SEKUND_MINUTT) 
    
    A_rørtverrsnitt = (pi/4)*D_rørdiameter
    v_fluidhastighet = Q_volumstrøm_m3_sekund / A_rørtverrsnitt
    
    f = f_rørfriksjonskoeffisent(
        ρ=ρ_vanntetthet,
        μ=μ_vannviskositet,
        v=v_fluidhastighet,
        d=D_rørdiameter,
        ε=ε_ruhetmeter,
    ) 

    hf_rørtapmeter      = f * (v_fluidhastighet**2/(2*g)) * (L_rørlengdemeter/D_rørdiameter) 
    h0_abluetapmeter    = K * (v_fluidhastighet**2/(2*g))
    Δhdyn_dynamisktrykk =     (v_fluidhastighet**2/(2*g)) - 0 # <- Antar ~ 0m/s ved toppen av tanken.
    
    # Bernouli 
    hp_pumpetrykk = ΔZ_høydemeter\
                  + Δhp_statisktrykk\
                  + Δhdyn_dynamisktrykk\
                  + hf_rørtapmeter\
                  + h0_albuetapmeter * antall_albuer

    return hp_pumptrykk


def f_rørfriksjonskoeffisent(ρ, v, d, μ, ε):
    """Gir en tilnærming til Moodys diagram for turbulent strømning Re > 4000"""
    from math import log10
    
    Re = (ρ*v*d)/μ

    A = 1/(3.7*(d/ε))
    B = 5.74/(Re**0.9)

    return 0.25 / (log10(A+B)**2)

        







    


    return;



if __name__ == "__main__":
    main()
