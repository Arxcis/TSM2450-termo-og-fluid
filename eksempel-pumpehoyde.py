from math import pi, log10

def main():
    #
    # Innstillinger
    #
    mu  = 2e-2   # Pas
    rho = 750    # kg/m3
    eps = 4.6e-5 # m
    eta = 0.6    # efficiency
    D1  = 1000   # m
    D2  = 0.25   # m
    P1  = 0      # kPa
    P2  = 150e3  # kPA
    Q   = 0.15   # m3/s
    z1  = 0      # m
    z2  = 2      # m
    L1  = 3      # m
    L2  = 10     # m
    g   = 9.81   # m2/s2
    Ktankexit = 0.5
    Kventil   = 0.19
    Kalbue    = 0.9
    Ks = [Ktankexit, Kventil, Kventil, Kalbue, Kalbue]

    #
    # Beregninger
    #
    A1 = (pi/4)*D1**2
    A2 = (pi/4)*D2**2
    v1 = Q/A1
    v2 = Q/A2
    print(f"v1: {v1:.3g}m/s, v2: {v2:.3g}m/s")

    re1 = Re(rho, v1, D1, mu)
    re2 = Re(rho, v2, D2, mu)
    print(f"Re1: {re1}, Re2: {re2}")

    f1 = f(D1, eps, re1)
    f2 = f(D2, eps, re2)
    print(f"f1: {f1}, f2: {f2}")

    hf1 = hf(f1, L1, D1, v1, g)
    hf2 = hf(f2, L2, D2, v2, g)
    print(f"hf1: {hf1}, hf2: {hf2}")
    
    h0 = h0sum(Ks, v2, g)
    hpress1 = hpress(P1, rho, g)
    hpress2 = hpress(P2, rho, g)
    hdyn1 = hdyn(v1, g)
    hdyn2 = hdyn(v2, g)
    print(f"hpress1: {hpress1:.3g}m, hpress2: {hpress2:.3g}m, hdyn1: {hdyn1:.3g}m, hdyn2: {hdyn2:.3g}m")
    print(f"hf1: {hf1:.3g}m, hf2: {hf2:.3g}m, z1: {z1}m, z2: {z2}m")

    hpumpe = hpress2 + hdyn2 + z2 - hpress1 - hdyn1 - z1 + hf1 + hf2 + h0
    print(f"hpumpe: {hpumpe}m")

    Ppumpe = (rho*g*hpumpe * Q) 
    Pel = Ppumpe / eta / 1000
    print(f"Volumstrøm: {Q}m3/s")
    print(f"            {Q*60*1000:.3g}lpm")
    print(f"Effekt pumpe = {Ppumpe/1000:.3g}kW")
    print(f"Effekt tilført = {Pel:.3g}kW")


def Re(rho, v, d, mu):
    """Reynoldstallet"""
    return (rho*v*d) / mu

def f(D, eps, Re):
    """Friksjonskoeffisienten"""
    if Re < 2000:
        return 64 / Re

    return 0.25 / (log10(1/(3.7*(D/eps)) + (5.74/Re**0.9)))**2

def hf(f, L, D, v, g):
    """Høydetap som resultat av friksjon"""
    return f * (L/D) * ((v**2)/(2*g))

def hpress(p, rho, g):
    """Statisk trykkhøyde"""
    return p / (rho*g)

def hdyn(v, g):
    """Dynamisk trykkhøyde"""
    return v**2/(2*g)

def h0sum(Ks, v, g):
    """Mindre tap komponent for komponent"""
    return sum(Ks)*((v**2)/(2*g))

if __name__ == "__main__":
    main()
