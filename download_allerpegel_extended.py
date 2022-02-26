import requests
import schedule
import datetime
import time
import os

def read_and_write_level():
	urlid = ["281", "213", "392", "223", "431", "148", "496", "593"]
	pegelname = ["Grafhorst", "Brenneckenbrück", "Langlingen", "Celle", "Marklendorf", "Ahlden", "Rethem", "Eitze"]
	flusskm = [127.26, 96.66, 82.20, 65.1, 41.32, 28.75, 17.65, 3.49]
	wasserstand = []
	
	jetzt = datetime.datetime.now()
	aktuelle_zeit = jetzt.strftime("%H:%M:%S")
	aktuelles_datum = jetzt.strftime("%Y-%m-%d")

	for i in range(len(pegelname)):
		r = requests.get("https://www.pegelonline.nlwkn.niedersachsen.de/Pegel/Binnenpegel/ID/" + urlid[i])
		page_content = str(r.text)
		pegel_aktuell = page_content[page_content.find("_0_Wasserstand_0")+18:page_content.find("_0_Wasserstand_0")+21]
		wasserstand.append(pegel_aktuell)
    
	print(wasserstand)
	
	csv_datei = open("aller_pegel_extended.csv", "a")

	for i in range(len(pegelname)):
		zeile = str(aktuelles_datum) + " " + str(aktuelle_zeit) + ";" + pegelname[i] + ";" + wasserstand[i] + "\n"
		csv_datei.write(zeile)
	csv_datei.close()

schedule.every().hour.do(read_and_write_level)

while True:
	schedule.run_pending()
	time.sleep(1)

