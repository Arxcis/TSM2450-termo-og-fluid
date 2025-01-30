
# TSM2450 Oblig 1

## Oppg 1

### Demo
```bash
jonas@pop-os:~/git/TSM2450-termo-og-fluid$ python oppg1.py

    Oppg1:

    Det skal kjøpes en olje/vann-separator lik den i bildet under. Det blå er vann (i bunn) og det beige er olje. Fra nær bunn går det ett rør oppover til å se nivået i tanken.

        a) Dersom oljen har en tetthet på 800 kg/m3 og har en høyde på 20cm, hva er da trykket i bunn av tanken om trykket i gassen i toppen er atmosfærisk?


        Svar:
          P_atmos =   101000.0 Pa
          P_olje  =     1569.6 Pa
          P_vann  =     7848.0 Pa
          P_over  =     9417.6 Pa
          P_abs   =   110417.6 Pa



        b) Dersom oljelaget kan forandre tykkelse, vil da røret for å se nivået fungere? Vis med formler og fysikk. Hint: Det er ikke olje i røret


        Svar: 1 ligning med 2 ukjente -> Dårlig måleprinsipp
```

## Oppg 2

### Demo
```bash
jonas@pop-os:~/git/TSM2450-termo-og-fluid$ python oppg2.py

Oppg2 svar:

    Innstillinger:
            areal              = 630 m2

            personer_per_areal = 0.7 stk
            personer 630m2     = 441 stk
            personer 160m2     = 112 stk
            personer  80m2     = 56 stk
            personer  70m2     = 49 stk
            personer  40m2     = 28 stk

            Q luft per time  =   26.0 m3/person/t
            Q luft per pers  = 0.0072 m3/person/s

            v_max = 10 m/s

    Rør:
        Total lengde = 66.00 m
        Total volum  =  9.94 m3

            Rom [m2]  Q [m3/s]  Lengde [m]  A min [m2]  A hylle [m2]  v hylle [m/s]
hoved            630     3.185         1.5       0.319         0.503          6.332
vestre           320     1.618        15.0       0.162         0.196          8.254
vestre 160       160     0.809         5.0       0.081         0.126          6.420
vestre 80         80     0.404         5.0       0.040         0.049          8.254
vestre 80         80     0.404         5.0       0.040         0.049          8.254
østre            310     1.567        15.0       0.157         0.196          7.996
østre 80         480     2.427         5.0       0.243         0.312          7.778
østre 80          80     0.404         5.0       0.040         0.049          8.254
østre 70          70     0.354         4.5       0.035         0.049          7.222
østre 40          40     0.202         5.0       0.020         0.031          6.523
```
