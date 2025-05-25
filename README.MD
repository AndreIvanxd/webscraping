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

