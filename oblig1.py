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

areal = 160 + 4*80 + 2*40 + 70 
personer_per_areal = 0.7 # person/m2
personer = areal * personer_per_areal

personer_160 = 160 * personer_per_areal
personer_80 = 80 * personer_per_areal
personer_70 = 70 * personer_per_areal
personer_40 = 40 * personer_per_areal

luft_pers_per_time = 26 # m3
luft_pers_per_sekund = luft_pers_per_time / 3600

luft_per_sekund = luft_pers_per_sekund * personer


print(f"""
    Svar:
        areal          = {int(areal)} m2
        personer       = {int(personer)} stk
        personer 160m2 = {personer_160:.0f} stk 
        personer  80m2 = {personer_80:.0f} stk
        personer  70m2 = {personer_70:.0f} stk 
        personer  40m2 = {personer_40:.0f} stk 

        luft per pers  = {luft_pers_per_sekund:.4f} m3/person/s
        luft total     = {luft_per_sekund:.2f} m3/s
      """)
