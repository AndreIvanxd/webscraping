# Andmete analüüs
![24_hour_chart2025-05-24.png](NordPoolProject/graafid/24_hour_chart2025-05-24.png)
![change_between_hours2025-05-24.png](NordPoolProject/graafid/change_between_hours2025-05-24.png)
![24_hour_chart2025-05-25.png](NordPoolProject/graafid/24_hour_chart2025-05-25.png)
![change_between_hours2025-05-25.png](NordPoolProject/graafid/change_between_hours2025-05-25.png)

Kasutan oma analüüsi jaoks kahe päeva tulemusi, et saada rohkem andmeid ja näitada korduvust.
Mõlemas päeva hinna graafis on näha sarnast mustrit. Vara hommikul ja öösetel aegadel on näha märgatavalt suuremat
hinda. Vaatades muutust tundide vahel teistelt graafidelt on näha, et umbes 1-st hakkab hind langema ja ei tõuse koradgi kuni 
keskpäev või õhtustel aegadel kus hind lendab lakke.


# Töö kirjeldus
Alustasin html lehe analüüsiga. Kuna leht on dünaamiline proovisin leida kohta kust saaks andmeid kätte. Kui leidsin üles
viisi kuidas andmeid kätte saada hakkasin kirjutama lahendust, et neid andmeid kätte saada.
Kasutasin Playwright raamistiku, et tekitada Chromiumi instance pythoni. Koos selle instancega sain ma ilusti välja töödelda 
vajalikud andmed. Kasutasin Pandas dataframe, et salvestada Kuupäev, tund ja hind. Kui andmed sain kätte tegin kaks funktsiooni
millega saan visualiseerida leitud andmeid. Esimene funktsioon teeb graafi 24 tunni jooksu muutustest ja teine funktsioon kujutab 
tulpdiagrammina iga tunnist muudatust hinnas. Samuti lisasin funktsiooni, mis võimaldab
tekitada dataframe lõppu rea, mis annab päevase summa.

# Kasutatud vahendid
Terve lahenduse kirjutasin pythonis, sest sellega on mul kõige rohkem kogemust ja python sobib väga hästi sellise ülesande lahendamiseks <br/>
Kasutasin pandas teeki, et andmeid salvestada, sest tundus kõige kergem viis salvestada andmed. Uurides dünaamilist web scrapingut
sain aru, et valikus on kas Selenium või Playwright. Otsustasin Playwrighti kasuks kuna sellega sai kergemini. 
Samuti Playwrightiga sai lihtsasti tõmmata Chromium browseri instance. Kasutasin visualiseerimiseks Matplotlibi, sest olen seda
kõige rohkem kasutanud

# Tulevased muudatused

Kui soovida automatiseerida andmete kogunemist, oleks vaja kuidagi iga päev vajalikke scripte runnida. Üks lahendusteks oleks
kasutada cloud service nagu näiteks AWS või Microsoft Azure. AWS lambdaga saaks automatiseerida skriptid ja kui tekitada nende andmete jaoks andmebaas
saaks otse sinna saata. Kui AWS on liiga ekstreemne lahendus saaks olla loov ja kasutada näiteks raspberry pi'd mis saab samuti
jooksutada antud koodi. Andmebaasi puhul sobiks midagi väga lihtsalt nagu PostgreSQL mis salvestaks päeva, kuu, tunni, hinna.

# Vajalikud vahendid ja tööle saamine
vajalik: Python
vajalikud teekid: matplotlib, pandas, playwright.sync_api
Need saab tõmmata näiteks **!pip install matplotlib pandas playwright** kui on olemas Python arvutis.
Samuti on vaja teha **playwright install**
Programmi saab windowsis tööle panna terminalist käsuga
**Python visualize.py (kuupäev) <br/>
Näide: Python visualize.py 2025-05-25**


