# Bibliographie-Daten 

Ziel des Projekts war die Anreicherung der Datenbank um bibliographische Daten des gemeinsame Verbundkatalog B3Kat des Bibliotheksverbundes Bayern (BVB) und des Kooperativen Bibliotheksverbundes Berlin-Brandenburg (KOBV). 
Diese liegen im MARCXML Format vor und können unter folgendem Link unter der Creative Commons License CC0 herunter geladen werden:
https://www.bib-bvb.de/web/b3kat/open-data (mittlerweile neuer Stand Nov 2021)

Liste über die Felder im MARC 21 Format: https://www.loc.gov/marc/bibliographic/

Kriterium für die Filterung war, dass an den Titeln beteiligte Personen in der Personen Mastertabelle der hismuslog Datenbank repräsentiert waren. 
Die GND-Ids der Personen aus der Datenbank liegen unter  "../data/gnd_ids.txt" vor.
Diese Ids wurden für das Matching benutzt. 

Alle Teile des B3Kat 2020 wurden für die Datenbank verarbeitet.
Die herausgefilterten Datensätze sind im CSV Format und haben folgende Informationen:
bvnumber,title,title_remainder,place,date,title_types,relationship,target,source

target und source sind die an dem Titel beteiligten Personen 
-> Sind mehr als zwei Personen aus der Datenbank beteiligt wird jeder mit jedem kombiniert

Ergebnisse unter: https://owncloud.gwdg.de/index.php/apps/files/?dir=/Fachgeschichte%20Musikwissenschaft/01-Datenbank/Arbeitspakete/Anreicherung_BSB_BMS/ergebnis_auf2021
Und in der Hismuslog Datenbank Relationentabelle: "rl-bvb-medien-beziehungen-pers-pers".

## Getting Started

### Setup (Conda)

```
# Erstellen
conda env create -f environment.yml

# Aktivieren
conda activate bibliographiedaten
```

### Setup (Linux)

```
make install

source venv/bin/activate
```

## Beispiel

```
1.
python command_line.py convert1  "../data/b3kat_export_2021_11_teil01.xml.gz" "../data/b3kat_export_2021_11_teil01.jsonl.gz"

2.
python command_line.py match "../data/gnd_ids.txt" "../data/b3kat_export_2021_11_teil01.jsonl.gz" "../data/test_all/result_on_b3kat_export_2021_11_teil01.xml.txt"

3.
python command_line.py convert2  "../data/test_all/result_on_b3kat_export_2021_11_teil01.xml.txt" "../data/test_all/result_on_b3kat_export_2021_11_teil01.xml.csv"

4.
python command_line.py merge "../data/test_all/" "../data/result/bibliographie_daten_all_parts.csv"

Datei "b3kat_export_2021_11_teil01.xml.gz" wurde als Beispiel heruntergeladen von: 
https://www.bib-bvb.de/web/b3kat/open-data 
```

## Anhang

### Conda Installation (Windows)

Installation von Miniconda

1. Herunterladen von [miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. Umgebungsvariablen anlegen (falls nicht automatisch)
    1. Umgebungsvariable `CONDA` anlegen mit Wert `path\to\Miniconda3\condabin`
    2. `%CONDA%` an die Umgebungsvariable `Path` anhängen

### Links

* [Conda Docs - Managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
