# TSM2450 Oblig 2

- Emne: Termo- og fluidmekanikk
- Tid: Vår 2025 USN Porsgrunn
- Repo: [https://github.com/Arxcis/TSM2450-oblig1](https://github.com/Arxcis/TSM2450-termo-og-fluid)


## Oppg1a)
![image](./bilder/oblig2-oppg1.png)

### Mål
Finne hvilket trykk, volumstrøm og effekt pumpen må ha for de tre dysene med strømningsfaktor = [17, 56, 107]. Det statiske trykket skal være 7.0bar overtrykk.

### Metode

For å finne volumstrømmen for en gitt dyse, benyttes følgende formel:
```math
Q  [dm3/min] = K \cdot \sqrt{p[bar overtrykk]}
```


### Resultat
```sh
oppg1.py  oppg2.py  README.md
(.venv) jonas@pop-os:~/git/TSM2450-termo-og-fluid/oblig2$ python oppg1.py
dysefaktor:  [ 17  56 107]
volumstrøm:  [0.00239338 0.00788408 0.01506423 0.005     ] [m3/sekund]
volumstrøm:  [143.60297516 473.04509465 903.85402013 300.        ] [l/min]
pumpetrykk:  [8.27656552 8.28711457 8.31655435 8.28027217] [Bar]
effekt:  [ 1980.89905577  6533.63149159 12528.25180008  4140.13608357] [Watt]
```

### Diskusjon



## Oppg1b)


## Oppg2
