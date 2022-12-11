from urllib.request import  urlopen
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
import numpy as np
def getAbschnitt(wort, index, liste):
    lage = ""

    while True:
        if wort in liste[index]:

            if not liste[index] == wort:
                if liste[index].startswith(wort) and len(liste.index())>len(wort):
                    liste[index] = liste[index].removeprefix(wort)
                    break
                lage += " " + liste[index].removesuffix(wort)

            index += 1
            break


        else:
            lage += " " + liste[index]
            index += 1
    return lage, index

def writeInCsv(datas, path):
    print(datas)

    with open(path, "w", encoding="UTF8", newline="\n") as f:
        print("Writing in csv: ")
        for dat in tqdm(datas):
            writer = csv.writer(f)
            writer.writerow(dat)

def getNextUrl(soup):
    urls = soup.select_one("#pagebrowser").select("a")
    if (urls[len(urls)-1].getText() != "Nächste >"):
        return -1
    return urls[len(urls) -1]["href"]
if __name__ == "__main__":
    header = ["Titel", "Datum", "Alamierungszeit", "Einsatzende", "Lage", "Einsatzort", "Stadtteil", "Fahrzeuge", "WeitereKraefte"]
    path = "D:/Datensätze/EinsatzberichteFeuerwehr/feuerwehr.csv"
    url = "https://www.feuerwehr-stadt-obertshausen.de/index.php?id=45"
    list = []
    list.append(header)


    i = 0
    print("Collecting: ")
    with tqdm(total=1967) as pbar:
        while True:
            page = urlopen(url)
            html_bytes = page.read()
            html = html_bytes.decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            inhalte = soup.select(".news-list-item")
            for inhalt in inhalte:
                try:
                    #print("\n\n")
                    h3 = inhalt.select_one("h3")
                    a = h3.select_one("a")
                    text = a.get_text()
                    parts = text.split(" — ")
                    datum = parts[0]
                    title = parts[1]
                    uri = "https://www.feuerwehr-stadt-obertshausen.de/" +a["href"]
                    soup2 = BeautifulSoup(urlopen(uri).read().decode("utf-8"), "html.parser")
                    innerText = soup2.select(".news-single-item2")[0]
                    parts2 = innerText.get_text().split("\n\n\n")
                    # print(parts2[0]) Title hab ich schon
                    beschreibung = parts2[1]
                    beschreibung.replace("&nbsp;", " ")
                    beschreibung.replace("\\xa0", " ")
                    partsBeschreibung = beschreibung.split(" ")
                    #print(partsBeschreibung)
                    start = partsBeschreibung[1].removesuffix("Einsatzende:")
                    ende = partsBeschreibung[2].removesuffix("Vorgefundene")
                    currentIndex = 4

                    lage, currentIndex = getAbschnitt("Einsatzort:", currentIndex, partsBeschreibung)  #Lage
                    ort, currentIndex = getAbschnitt("Stadtteil:", currentIndex, partsBeschreibung) # Ort
                    stadtteil, currentIndex = getAbschnitt("Eingesetzte", currentIndex, partsBeschreibung)
                    currentIndex += 1 # Eingesetzte Fahrzeuge zwei woerter
                    fahrzeuge, currentIndex = getAbschnitt("Weitere", currentIndex, partsBeschreibung)
                    currentIndex += 1 # Weiter Kräfte zwei Woerter
                    weitereKraefte, currentIndex = getAbschnitt("Einsatzbericht:", currentIndex, partsBeschreibung)
                    data = [title, datum, start, ende, lage, ort, stadtteil, fahrzeuge, weitereKraefte]
                except Exception as e:
                    # print(e)
                    pbar.update(1)
                    i += 1
                    continue



                list.append(data)
                i+=1


                """
                print(title)
                print(datum)
                print(start)
                print(ende)
                print(lage)
                print(ort)
                print(stadtteil)
                print(fahrzeuge)
                print(weitereKraefte)
                print()
                print()
                print("###############################################")
                print()
                """


                pbar.update(1)

            urlPart = getNextUrl(soup)
            if (urlPart == -1):
                break
            url = "https://www.feuerwehr-stadt-obertshausen.de/"+urlPart
            #print(url)
    writeInCsv(list, path)
