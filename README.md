# Akciju cenu prognozēšana
## Anna Sotņikova 231RDB267
### Projekta uzdevums:
Šis projekts ir paredzēts akciju cenu prognozēšanu, izmantojot Python un lineārās regresijas modeli. Projekta mērķis ir izstrādāt precīzu un efektīvu modeli, kas spēj prognozēt akciju cenas nākotnē. Projekta pamatā ir vēsturisko datu izmantošana. Šie dati tiek iegūti no **Yahoo Finance**, rūpīgi apstrādāti un sagatavoti tālākai izmantošanai. Dati ietver informāciju par akciju cenām dažādos laika periodos.

Pamatojoties uz šiem datiem, tiek apmācīts lineārās regresijas modelis. Modelis spēj mācīties no datiem un pielāgoties mainīgajai situācijai akciju tirgū. Tas tiek darīts, izmantojot **scikit-learn** bibliotēku, kas ir populāra mašīnmācīšanās bibliotēka Python valodā. 

Pēc modeļa apmacīšanas, tas tiek izmantots, lai prognozētu akciju cenas nākamajām 10 dienām. Prognozes tiek veiktas, izmantojot modeļa iegūtās zināšanas par iepriekšējo akciju cenu dinamiku. 

Turklāt, šis projekts ietver arī vizualizācijas komponenti. Izstrādātais modelis var izveidot grafiku, kas parāda gan faktiskās, gan prognozētās akciju cenas. Tas tiek darīts, izmantojot **matplotlib** bibliotēku, kas ir viena no visplašāk izmantotajām zinātniskās vizualizācijas bibliotēkām Python valodā.

Visbeidzot, šis projekts ietver arī funkcionalitāti, kas ļauj saglabāt gan faktiskās, gan prognozētās akciju cenas **Excel** failā. Tas nodrošina iespēju viegli analizēt un salīdzināt datus ārpus Python vides. 

Šis projekts ir lielisks piemērs tam, kā var izmantot Python valodu un tās bibliotēkas, lai risinātu sarežģītus uzdevumus, piemēram, akciju cenu prognozēšanu. Tas parāda Python valodas spēju apvienot datu ieguvi, apstrādi, modelēšanu, vizualizāciju un saglabāšanu vienā integrētā procesā.
### Izmantotas Python bibliotēkas:
- Pandas
```python
import pandas as pd
```
**Pandas** ir ātrs, jaudīgs, elastīgs un viegli lietojams atvērtā koda datu analīzes un manipulācijas rīks, kas ir veidots uz Python programmēšanas valodas bāzes. Tas nodrošina datu struktūras un funkcijas, kas nepieciešamas strukturētu datu apstrādei, tostarp funkcionalitāti skaitlisko tabulu un laika rindu datu apstrādei. Mana kodā tas tiek izmantots datu un datumu apstrādei **(pd.date_range)**.
- Yfinance
```python
import yfinance as yf
```
**Yfinance** ir Python bibliotēka, kas ļauj piekļūt Yahoo Finance pieejamajiem finanšu datiem. Tā piedāvā pavedienu un Pythonic veidu, kā lejupielādēt tirgus datus no Yahoo! Finance. Tas ir atvērtā koda rīks, kas izmanto Yahoo publiski pieejamās API un ir paredzēts pētniecības un izglītības mērķiem.
- NumPy
```python
import numpy as np
```
**Numpy** ir Python bibliotēka, kas nodrošina atbalstu lieliem, daudzdimensiju masīviem un matricām, kā arī lielu augsta līmeņa matemātisko funkciju kolekciju darbam ar šiem masīviem. To izmanto zinātniskajiem aprēķiniem Python. Tā nodrošina rīkus darbam ar šiem masīviem un lielu skaitļošanas efektivitāti. Kodā tas tiek izmantots, lai izveidotu datumu masīvu prognozēšanai.
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
**Sklearn (scikit-learn)** ir Python modulis mašīnmācīšanās procesam, kas veidots uz **SciPy** bāzes. Tas nodrošina vienkāršus un efektīvus rīkus prognozēšanas datu analīzei. Tas atbalsta dažādus mašīnmācīšanās algoritmus, piemēram, klasifikāciju, regresiju, klasterizāciju un citus. Tas ir izstrādāts tā, lai sadarbotos ar Python skaitlisko un zinātnisko bibliotēku **NumPy** un **SciPy**. Mana kodā **train_test_split** funkcija tiek izmantota, lai datu kopu sadalītu nejaušās apmācības un testa apakškopās un **LinearRegression** tiek izmantots, lai izveidotu lineārās regresijas modeli akciju cenu prognozēšanai.
- Matplotlib
```python
import matplotlib.pyplot as plt
```
**Matplotlib** ir visaptveroša bibliotēka statisku, animētu un interaktīvu vizualizāciju izveidei Python. Tā rada publikāciju kvalitātes attēlus dažādos formātos un platformās, un to var izmantot skriptos, čaulās, tīmekļa lietojumprogrammās un grafiskās lietotāja saskarnes rīku komplektos. Tā ir attēlošanas bibliotēka Python programmēšanas valodai un tās skaitliskās matemātikas paplašinājumam **NumPy**. Kodā tas tiek izmantots, lai attēlotu faktiskās un prognozētās akciju cenas.

Katrai bibliotēkai ir noteikta loma, un kopā tās palīdz iegūt, apstrādāt, modelēt un vizualizēt datus.
### Programmatūras izmantošanas metodes:
Šī programmatūra ir rīks investoriem, kuri meklē zinātniski pamatotu metodi akciju cenu prognozēšanai. Tā palīdzēs investoriem pieņemt labākus lēmumus un palielināt peļņu. 

Lai izmantotu šo programmatūru, ir jāinstalē nepieciešamās bibliotēkas, kas ietver **pandas**, **yfinance**, **numpy**, **datetime**, **timedelta**, **sklearn.model_selection**, **sklearn.linear_model** un **matplotlib.pyplot**. Šīs bibliotēkas nodrošina nepieciešamo funkcionalitāti datu ieguvei, apstrādei, modelēšanai un vizualizācijai.

Papildus tam, ir jānodrošina piekļuve Yahoo Finance datiem. **Yahoo Finance** ir viens no vadošajiem finanšu portāliem, kas nodrošina plašu spektru finanšu tirgus datu, tostarp akciju cenas, obligācijas, valūtas kursus un citu informāciju.

Pēc tam, kad ir instalētas visas nepieciešamās bibliotēkas un nodrošināta piekļuve datiem, var mainīt tikera simbolu un datumus atbilstoši savām vajadzībām. Tikera simbols ir unikāls identifikators, kas tiek izmantots, lai atpazītu konkrētu akciju tirgū. Datumi tiek izmantoti, lai noteiktu vēsturisko periodu, par kuru tiek iegūti dati.

Kad šie soļi ir izpildīti, var palaist programmatūru un skatīt prognozētās cenas diagrammā un saglabāt tās Excel failā. Diagramma ļauj vizuāli salīdzināt faktiskās un prognozētās cenas, kas var palīdzēt investoriem labāk izprast tirgus tendences. Excel fails nodrošina iespēju saglabāt un analizēt datus ārpus Python vides, kas var būt noderīgi tālākai analīzei un lēmumu pieņemšanai.

Šī programmatūra ir lielisks rīks gan pieredzējušiem, gan jauniem investoriem, kuri vēlas izmantot zinātniski pamatotas metodes, lai prognozētu akciju cenas un veiktu informētus lēmumus. Tā ir izstrādāta, lai būtu viegli lietojama un pielāgojama dažādām vajadzībām, un tā var būt vērtīgs papildinājums jebkura investora rīku kastītei.
