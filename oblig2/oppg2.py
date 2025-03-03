


def main():
    #
    # Forutsetninger
    #
    rho_vann = 1000
    Q_liter = 4.0
    Q_m3 = Q_liter / (1000*60)
    p_inn = 0.2e5
    D_inn = 10e-3
    D_ut  = 3e-3
    
    #
    # Beregninger
    #
    from math import pi, atan
    A_inn = (pi/4)*D_inn**2
    A_ut  = (pi/4)*D_ut**2

    v_inn = Q_m3/A_inn
    v_ut  = Q_m3/A_ut
    

    # Bernouli / energiloven
    """
    p_ut + p_dynamisk_ut = p_inn + p_dynamisk_inn
    p_ut = p_inn + p_dynamisk_inn - p_dynamisk_ut
    p_ut = p_inn + (rho/2)(v_inn^2 - v_ut^2)
    """
    p_ut = p_inn + (rho_vann/2) * (v_inn**2 - v_ut**2) 

    # Newtons 2. og 3. lov
    """
    sum(F) = m * a
           = kg * m/(s*s)
           = kg/s * m/s
           = kg/m3 * m3/s * m/s
           = rho   * Q    * v
    sum(F) = F - Fmotkraft
        -p_inn*A_inn + Rx = rho * Q * (-v_inn)
        -p_ut*A_ut + Ry = rho * Q * (v_ut)
    """
    Rx = rho_vann*Q_m3*(-v_inn) + p_inn*A_inn
    Ry = rho_vann*Q_m3*(v_ut) + p_ut*A_ut
    α = (atan(Ry/Rx)/pi) * 180
    
    #
    # Resultat
    #
    print(f"""
        {"Q_liter":<7} {Q_liter:10.3g} liter/min,
        {"v_inn":<7} {v_inn:10.3g} m/s,
        {"v_ut":<7} {v_ut:10.3g} m/s,
        {"p_inn":<7} {p_inn:10.3g} Pa,
        {"p_ut":<7} {p_ut:10.3g} Pa,
        {"Rx":<7} {Rx:10.3g} N,
        {"Ry":<7} {Ry:10.3g} N,
        {"α":<7} {α:10.3g} °,
    """)

if __name__ == "__main__":

    main()