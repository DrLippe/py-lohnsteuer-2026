# Lohnsteuer 2026 – PAP in Python für Excel

Python-Umsetzung des **BMF-Programmablaufplans für die maschinelle Lohnsteuerberechnung 2026** (PAP 2026). Standardbibliothek `decimal`, keine externen Python-Abhängigkeiten.

## Dateien

- `lohnsteuer2026.py`: PAP-Berechnungsroutinen mit `Decimal` und Excel-Adapter
- `tests/test_pap2026.py`: Regressionstest mit BMF-Referenzbeispiel

## Python-Anwendung

```python
from lohnsteuer2026 import pap2026, lohnsteuer_excel

# Originale PAP-Einheiten: RE4 in Cent, LZZ=2 für Monatslohn
x = pap2026(LZZ=2, RE4=500000, STKL=1, KVZ=2.5, PVZ=1)
print(x["LSTLZZ"])  # 78583 Cent (BMF-Referenzbeispiel)

# Benutzerfreundlich: Euro statt Cent
x = lohnsteuer_excel(
    brutto_eur=5000,
    steuerklasse=1,
    zeitraum=2,
    kv_zusatzbeitrag=2.5,
    pv_kinderlos=1,
)
print(x["LSTLZZ"])  # 785.83 EUR
```

**Bitte beachten:** Die angegebenen PAP-Flags (insbesondere `KRV`, `PKV`, `PVZ`, `PVS`, `KVZ`) müssen zur tatsächlichen Versicherungssituation passen. Ausgangswerte dienen lediglich dem Beispiel.

### Bedeutung der wichtigsten Felder

| Parameter | Bedeutung |
|---|---|
| `RE4` | laufender steuerpflichtiger Arbeitslohn im Lohnzahlungszeitraum, **Cent** |
| `STKL` | Steuerklasse 1 bis 6 |
| `LZZ` | 1 = Jahr, 2 = Monat, 3 = Woche, 4 = Tag |
| `KVZ` | KV-Zusatzbeitrag als Prozentwert, etwa `2.5` |
| `PVZ` | 1 = PV-Zuschlag für Kinderlose, 0 = nein |
| `PVS` | 1 = Sachsen, 0 = sonst |
| `ZKF` | Zahl der Kinderfreibeträge, etwa `0.5`, `1` |
| `KRV` | Original-PAP-Kennzeichen zur Rentenversicherung |
| `PKV` | Original-PAP-Kennzeichen zur Krankenversicherung |
| `JFREIB` | Jahresfreibetrag in Cent |
| `LSTLZZ` | Lohnsteuer des Zeitraums in Cent |
| `SOLZLZZ` | Solidaritätszuschlag des Zeitraums in Cent |
| `BK` | Bemessungsgrundlage für Kirchenlohnsteuer, **nicht** Kirchensteuerbetrag |

Die Funktion `pap2026` gibt alle offiziellen Ausgabewerte in Cent aus. `lohnsteuer_excel` nimmt `brutto_eur`, `freibetrag_jahr_eur` und `hinzurechnung_jahr_eur` in Euro entgegen und gibt die Ergebnisse in Euro zurück. Andere optionale PAP-Werte via `**pap_parameter` bleiben in den **Original-PAP-Einheiten**.

## Verwendung in *Python in Excel* (Microsoft 365)

Python in Excel läuft in der Microsoft-Cloud und kann lokale Python-Dateien nicht regulär über `import lohnsteuer2026` laden. Am einfachsten:

1. Den **vollständigen Inhalt** von `lohnsteuer2026.py` kopieren.
2. In einer Python-in-Excel-Zelle als Definitionscode einfügen (nicht in eine normale Excel-Zelle).
3. In einer **nachfolgenden Python-Zelle** die Funktion verwenden:

```python
lohnsteuer_excel(
    brutto_eur=xl("B2"),
    steuerklasse=xl("B3"),
    zeitraum=2,
    kv_zusatzbeitrag=xl("B4"),
    pv_kinderlos=1,
)["LSTLZZ"]
```

Das Ergebnis ist ein Euro-Betrag. Für mehrere Ergebnisfelder kannst du die Funktion mit unterschiedlichen Schlüsseln aufrufen. Verwende explizit eine PY-Zelle, um die Python-Funktionen auszuführen. Wie die Ausgabe in die Excel-Arbeitsmappe übernommen wird, hängt von der Python-Ausgabe-Einstellung ab.

**Wichtig:** Der PAP ermittelt Lohnsteuer, Solidaritätszuschlag und Kirchensteuer-Bemessungsgrundlagen, **nicht** den vollständigen Nettolohn und nicht die abzuführende Kirchensteuer. Die übrigen Sozialabgaben müssen separat berechnet werden.

## Herkunft und Verifikation

Die Berechnungsfunktionen stammen aus der auf amtlichem BMF-XML basierenden generierten Python-Umsetzung [C-0711/babu](https://github.com/C-0711/babu/blob/main/server/belegreview/lohnsteuer_pap.py); der Excel-Adapter und die Tests sind zusätzliche Projektdateien. Den Quelltext auf korrekte Verwendung und Lizenz vor einer Weiterveröffentlichung prüfen. Der algorithmische PAP ist eine amtliche Vorlage; externe Projektbestandteile können anderen Lizenzbedingungen unterliegen.

- [Offizieller BMF-PAP 2026 (XML)](https://www.bmf-steuerrechner.de/javax.faces.resource/daten/xmls/Lohnsteuer2026.xml.xhtml)
- [BMF-Veröffentlichung 12.11.2025](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026.html)
- [BMF-Schnittstellenbeschreibung](https://www.bmf-steuerrechner.de/interface/pseudocodes.xhtml)

**Teststatus:** Der Referenzwert ist als Regressionstest erfasst. Für produktiven Einsatz sollten weitere Kombinationen aller Steuerklassen, Lohnzahlungszeiträume, Versicherungskennzeichen, Freibeträge und sonstigen Bezüge mit der amtlichen BMF-Schnittstelle abgeglichen werden.
