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

