# Akciju cenu prognozēšana
## Anna Sotņikova 231RDB267
### Projekta uzdevums:
Šis projekts ir paredzēts akciju cenu prognozēšanu, izmantojot Python un lineārās regresijas modeli. Projekta mērķis ir izstrādāt precīzu un efektīvu modeli, kas spēj prognozēt akciju cenas nākotnē. Projekta pamatā ir vēsturisko datu izmantošana. Šie dati tiek iegūti, rūpīgi apstrādāti un sagatavoti tālākai izmantošanai. Dati ietver informāciju par akciju cenām dažādos laika periodos. Pamatojoties uz šiem datiem, tiek apmācīts lineārās regresijas modelis. Modelis spēj mācīties no datiem un pielāgoties mainīgajai situācijai akciju tirgū. Pēc modeļa apmacīšanas, tas tiek izmantots, lai prognozētu akciju cenas nākamajām 10 dienām. 
### Izmantotas Python bibliotēkas:
- Pandas
```python
import pandas as pd
```
**Pandas** ir bibliotēka datu manipulācijai un analīzei. Tā piedāvā datu struktūras un operācijas datu tabulu manipulēšanai un analīzei.
- Yfinance
```python
import yfinance as yf
```
**Yfinance** ir bibliotēka, kas ļauj viegli iegūt Yahoo Finance datus.
- NumPy
```python
import numpy as np
```
**NumPy** ir bibliotēka, kas piedāvā atbalstu lieliem, daudzdimensiju masīviem un matricām, kā arī augsta līmeņa matemātiskām funkcijām, lai strādātu ar šiem masīviem.
- Datetime
```python
from datetime import datetime, timedelta
```
**Datetime** un **Timedelta** moduļi nodrošina funkcijas datumu un laika manipulācijai.
- Sklearn
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
```
**Train_test_split** ir funkcija no **sklearn.model_selection**, kas sadala datus treniņa un testa kopās. **LinearRegression** ir klase no **sklearn.linear_model**, kas ļauj veikt lineārās regresijas modelēšanu.
- Matplotlib
```python
import matplotlib.pyplot as plt
```
**Matplotlib.pyplot** ir bibliotēka, kas nodrošina objektorientētu API grafiku zīmēšanai Python programmās.
### Programmatūras izmantošanas metodes:
Šī programmatūra ir rīks investoriem, kuri meklē zinātniski pamatotu metodi akciju cenu prognozēšanai. Tā palīdzēs investoriem pieņemt labākus lēmumus un palielināt peļņu.
