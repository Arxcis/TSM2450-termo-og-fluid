
# TSM2450 Oblig 1

* Emne: Termo- og fluidmekanikk
* Tid: Vår 2025 USN Porsgrunn
* Repo: https://github.com/Arxcis/TSM2450-oblig1

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
```

## Oppg 2

### Demo
```bash
jonas ~/git/TSM2450-oblig1 $ python oppg2.py

#
# Oppg2 svar:
#

Innstillinger:
    V max            =     10.0 m/s
    Q luft per time  =     26.0 m3/person/t
    
                Lengde [m]  Areal [m2]
    hoved              1.5         630
    vestre            15.0         320
    vestre 160         5.0         160
    vestre 80          5.0          80
    vestre 80          5.0          80
    østre             15.0         310
    østre 80           5.0          80
    østre 80           5.0          80
    østre 70           4.5          70
    østre 40           5.0          40

Beregninger:
    Q luft per sekund = 0.0072 m3/person/s

    Total personer  =    441 stk
    Total romareal  = 630.00 m2
    Total rørlengde =  66.00 m
    Total rørvolum  =   8.62 m3
        
                Personer  Q [m3/s]  A min [m2]  A hylle [m2]  len [m]  volum [m3]  v hylle [m/s]
    hoved            441     3.185       0.319         0.503      1.5       0.754          6.332
    vestre           224     1.618       0.162         0.196     15.0       2.940          8.254
    vestre 160       112     0.809       0.081         0.126      5.0       0.630          6.420
    vestre 80         56     0.404       0.040         0.049      5.0       0.245          8.254
    vestre 80         56     0.404       0.040         0.049      5.0       0.245          8.254
    østre            217     1.567       0.157         0.196     15.0       2.940          7.996
    østre 80          56     0.404       0.040         0.049      5.0       0.245          8.254
    østre 80          56     0.404       0.040         0.049      5.0       0.245          8.254
    østre 70          49     0.354       0.035         0.049      4.5       0.221          7.222
    østre 40          28     0.202       0.020         0.031      5.0       0.155          6.523
```