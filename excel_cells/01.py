"""Lohnsteuer nach dem amtlichen Programmablaufplan 2026.

ERZEUGT — NICHT VON HAND ÄNDERN.

Übersetzt aus dem XML-Pseudocode des BMF (Lohnsteuer2026) durch
`werkzeug/pap_uebersetzen.py`. Wer hier etwas ändert, verliert es beim
nächsten Jahreswechsel und weicht außerdem vom amtlichen Ablauf ab.

Der Programmablaufplan ist ein amtliches Werk (§ 5 UrhG). Die Namen der
Felder und Methoden sind seine, nicht unsere — deshalb stehen sie hier
groß und unübersetzt: nur so lässt sich Zeile für Zeile mit dem Original
vergleichen.

Gerechnet wird mit `Decimal`, weil Java `BigDecimal` verwendet. Mit
Fließkomma käme man auf Centbeträge, die um einen Cent danebenliegen — und
in einer Lohnabrechnung fällt genau das auf.
"""
from __future__ import annotations

from decimal import Decimal as D, ROUND_DOWN, ROUND_UP, getcontext

# Java rechnet Divisionen ohne Skalenangabe exakt. Genug Stellen, damit
# Python dasselbe tut.
getcontext().prec = 60


def stellen(wert: D, n: int, rundung: str) -> D:
    """Java: setScale(n, rundung)."""
    return wert.quantize(D(1).scaleb(-n), rounding=rundung)


def teilen(a: D, b: D, n: int, rundung: str) -> D:
    """Java: divide(b, n, rundung)."""
    return stellen(a / b, n, rundung)


def vergleiche(a: D, b: D) -> int:
    """Java: compareTo — minus eins, null oder eins."""
    return (a > b) - (a < b)


class Zustand:
    """Alle Felder des Ablaufplans an einer Stelle.

    Ein Objekt statt vieler Parameter: der Ablaufplan schreibt quer durch
    seine Unterprogramme in gemeinsame Felder, und das soll die Übersetzung
    nicht verstecken.
    """

    __slots__ = ("AJAHR", "ALTE", "ALTER1", "ALV", "ANP", "ANTEIL1", "AVSATZAN", "BBGKVPV", "BBGRVALV", "BK", "BKS", "BMG", "DIFF", "EFA", "FVB", "FVBSO", "FVBZ", "FVBZSO", "GFB", "HBALTE", "HFVB", "HFVBZ", "HFVBZSO", "HOCH", "J", "JBMG", "JFREIB", "JHINZU", "JLFREIB", "JLHINZU", "JRE4", "JRE4ENT", "JVBEZ", "JW", "K", "KFB", "KRV", "KVSATZAN", "KVZ", "KZTAB", "LSTJAHR", "LSTLZZ", "LSTOSO", "LSTSO", "LZZ", "LZZFREIB", "LZZHINZU", "MBV", "MIST", "PKPV", "PKPVAGZ", "PKPVAGZJ", "PKV", "PVA", "PVS", "PVSATZAN", "PVZ", "R", "RE4", "RVSATZAN", "RW", "SAP", "SOLZFREI", "SOLZJ", "SOLZLZZ", "SOLZMIN", "SOLZS", "SOLZSBMG", "SOLZSZVE", "SONSTB", "SONSTENT", "ST", "ST1", "ST2", "STERBE", "STKL", "STS", "VBEZ", "VBEZB", "VBEZBSO", "VBEZM", "VBEZS", "VBS", "VERGL", "VFRB", "VFRBS1", "VFRBS2", "VJAHR", "VSP", "VSPALV", "VSPHB", "VSPKVPV", "VSPN", "VSPR", "W1STKL5", "W2STKL5", "W3STKL5", "WVFRB", "WVFRBM", "WVFRBO", "X", "Y", "ZKF", "ZMVB", "ZRE4", "ZRE4J", "ZRE4VP", "ZRE4VPR", "ZTABFB", "ZVBEZ", "ZVBEZJ", "ZVE", "ZX", "ZZX", "af", "f")

    def __init__(self, **eingaben):
        self.AJAHR = 0
        self.ALTE = D("0")
        self.ALTER1 = 0
        self.ALV = 0
        self.ANP = D("0")
        self.ANTEIL1 = D("0")
        self.AVSATZAN = D("0")
        self.BBGKVPV = D("0")
        self.BBGRVALV = D("0")
        self.BK = D("0")
        self.BKS = D("0")
        self.BMG = D("0")
        self.DIFF = D("0")
        self.EFA = D("0")
        self.FVB = D("0")
        self.FVBSO = D("0")
        self.FVBZ = D("0")
        self.FVBZSO = D("0")
        self.GFB = D("0")
        self.HBALTE = D("0")
        self.HFVB = D("0")
        self.HFVBZ = D("0")
        self.HFVBZSO = D("0")
        self.HOCH = D("0")
        self.J = 0
        self.JBMG = D("0")
        self.JFREIB = D("0")
        self.JHINZU = D("0")
        self.JLFREIB = D("0")
        self.JLHINZU = D("0")
        self.JRE4 = D("0")
        self.JRE4ENT = D("0")
        self.JVBEZ = D("0")
        self.JW = D("0")
        self.K = 0
        self.KFB = D("0")
        self.KRV = 0
        self.KVSATZAN = D("0")
        self.KVZ = D("0")
        self.KZTAB = 0
        self.LSTJAHR = D("0")
        self.LSTLZZ = D("0")
        self.LSTOSO = D("0")
        self.LSTSO = D("0")
        self.LZZ = 1
        self.LZZFREIB = D("0")
        self.LZZHINZU = D("0")
        self.MBV = D("0")
        self.MIST = D("0")
        self.PKPV = D("0")
        self.PKPVAGZ = D("0")
        self.PKPVAGZJ = D("0")
        self.PKV = 0
        self.PVA = D("0")
        self.PVS = 0
        self.PVSATZAN = D("0")
        self.PVZ = 0
        self.R = 0
        self.RE4 = D("0")
        self.RVSATZAN = D("0")
        self.RW = D("0")
        self.SAP = D("0")
        self.SOLZFREI = D("0")
        self.SOLZJ = D("0")
        self.SOLZLZZ = D("0")
        self.SOLZMIN = D("0")
        self.SOLZS = D("0")
        self.SOLZSBMG = D("0")
        self.SOLZSZVE = D("0")
        self.SONSTB = D("0")
        self.SONSTENT = D("0")
        self.ST = D("0")
        self.ST1 = D("0")
        self.ST2 = D("0")
        self.STERBE = D("0")
        self.STKL = 1
        self.STS = D("0")
        self.VBEZ = D("0")
        self.VBEZB = D("0")
        self.VBEZBSO = D("0")
        self.VBEZM = D("0")
        self.VBEZS = D("0")
        self.VBS = D("0")
        self.VERGL = D("0")
        self.VFRB = D("0")
        self.VFRBS1 = D("0")
        self.VFRBS2 = D("0")
        self.VJAHR = 0
        self.VSP = D("0")
        self.VSPALV = D("0")
        self.VSPHB = D("0")
        self.VSPKVPV = D("0")
        self.VSPN = D("0")
        self.VSPR = D("0")
        self.W1STKL5 = D("0")
        self.W2STKL5 = D("0")
        self.W3STKL5 = D("0")
        self.WVFRB = D("0")
        self.WVFRBM = D("0")
        self.WVFRBO = D("0")
        self.X = D("0")
        self.Y = D("0")
        self.ZKF = D("0")
        self.ZMVB = 0
        self.ZRE4 = D("0")
        self.ZRE4J = D("0")
        self.ZRE4VP = D("0")
        self.ZRE4VPR = D("0")
        self.ZTABFB = D("0")
        self.ZVBEZ = D("0")
        self.ZVBEZJ = D("0")
        self.ZVE = D("0")
        self.ZX = D("0")
        self.ZZX = D("0")
        self.af = 1
        self.f = D("1.0")
        for name, wert in eingaben.items():
            if name not in self.__slots__:
                raise AttributeError(f"{name} kennt der Ablaufplan nicht")
            setattr(self, name, wert if isinstance(wert, (D, int)) else D(str(wert)))


# ————— Konstanten des Ablaufplans —————
TAB1 = [D("0"), D("0.4"), D("0.384"), D("0.368"), D("0.352"), D("0.336"), D("0.32"), D("0.304"), D("0.288"), D("0.272"), D("0.256"), D("0.24"), D("0.224"), D("0.208"), D("0.192"), D("0.176"), D("0.16"), D("0.152"), D("0.144"), D("0.14"), D("0.136"), D("0.132"), D("0.128"), D("0.124"), D("0.12"), D("0.116"), D("0.112"), D("0.108"), D("0.104"), D("0.1"), D("0.096"), D("0.092"), D("0.088"), D("0.084"), D("0.08"), D("0.076"), D("0.072"), D("0.068"), D("0.064"), D("0.06"), D("0.056"), D("0.052"), D("0.048"), D("0.044"), D("0.04"), D("0.036"), D("0.032"), D("0.028"), D("0.024"), D("0.02"), D("0.016"), D("0.012"), D("0.008"), D("0.004"), D("0")]