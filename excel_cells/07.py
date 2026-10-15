def UPTAB26(z: Zustand) -> None:
    if (vergleiche(z.X, (z.GFB + ZAHL1)) == (-D("1"))):
        z.ST = D("0")
    else:
        if (vergleiche(z.X, D("17800")) == (-D("1"))):
            z.Y = teilen(((z.X - z.GFB)), ZAHL10000, D("6"), 'ROUND_DOWN')
            z.RW = (z.Y * D("914.51"))
            z.RW = (z.RW + D("1400"))
            z.ST = stellen(((z.RW * z.Y)), D("0"), 'ROUND_DOWN')
        else:
            if (vergleiche(z.X, D("69879")) == (-D("1"))):
                z.Y = teilen(((z.X - D("17799"))), ZAHL10000, D("6"), 'ROUND_DOWN')
                z.RW = (z.Y * D("173.1"))
                z.RW = (z.RW + D("2397"))
                z.RW = (z.RW * z.Y)
                z.ST = stellen(((z.RW + D("1034.87"))), D("0"), 'ROUND_DOWN')
            else:
                if (vergleiche(z.X, D("277826")) == (-D("1"))):
                    z.ST = stellen(((((z.X * D("0.42"))) - D("11135.63"))), D("0"), 'ROUND_DOWN')
                else:
                    z.ST = stellen(((((z.X * D("0.45"))) - D("19470.38"))), D("0"), 'ROUND_DOWN')
    z.ST = (z.ST * D(z.KZTAB))


def berechnen(z: Zustand) -> Zustand:
    """Der Hauptlauf des Ablaufplans."""
    MPARA(z)
    MRE4JL(z)
    z.VBEZBSO = D("0")
    MRE4(z)
    MRE4ABZ(z)
    MBERECH(z)
    MSONST(z)
    return z



# Excel-friendly wrapper: all monetary arguments in EUR unless noted.
# Internally the PAP uses integer cents for monetary inputs/outputs.
_PAP_DECIMAL_INPUTS = {
    "JFREIB", "JHINZU", "JRE4", "JRE4ENT", "JVBEZ", "LZZFREIB",
    "LZZHINZU", "MBV", "PKPV", "PKPVAGZ", "RE4", "SONSTB",
    "SONSTENT", "STERBE", "VBEZ", "VBEZM", "VBEZS", "VBS", "ZMVB",
}
_PAP_RATIO_INPUTS = {"KVZ", "PVA", "ZKF", "f"}
_PAP_INPUTS = _PAP_DECIMAL_INPUTS | _PAP_RATIO_INPUTS | {
    "af", "AJAHR", "ALTER1", "ALV", "KRV", "LZZ", "PKV",
    "PVS", "PVZ", "R", "STKL", "VJAHR",
}
_PAP_OUTPUTS = ("LSTLZZ", "SOLZLZZ", "BK", "STS", "SOLZS", "BKS",
                "VFRB", "VFRBS1", "VFRBS2", "WVFRB", "WVFRBO", "WVFRBM")


def pap2026(**inputs):
    """Official PAP fields: money in CENTS; outputs are integer CENTS.

    Example: pap2026(LZZ=2, RE4=500000, STKL=1, KVZ=2.5, PVZ=1).
    Missing inputs use the PAP defaults; set your actual insurance flags.
    """
    unknown = set(inputs) - _PAP_INPUTS
    if unknown:
        raise ValueError("Unknown PAP input(s): " + ", ".join(sorted(unknown)))
    values = {}
    for key, value in inputs.items():
        if value is None or value == "":
            continue
        values[key] = D(str(value)) if key in _PAP_DECIMAL_INPUTS | _PAP_RATIO_INPUTS else int(value)
    z = Zustand(**values)
    berechnen(z)
    return {key: int(getattr(z, key)) for key in _PAP_OUTPUTS}


def lohnsteuer_excel(brutto_eur, steuerklasse=1, *,
                     zeitraum=2, kv_zusatzbeitrag=2.9, pv_kinderlos=1,
                     pv_sachsen=0, pv_kinder=0, rentenversicherung=0,
                     krankenversicherung=0, freibetrag_jahr_eur=0,
                     hinzurechnung_jahr_eur=0, kirchensteuer=0, **pap_parameter):
    """Easy Excel entry point. Amounts in EUR; returns result values in EUR.

    zeitraum: 1=year, 2=month, 3=week, 4=day.
    kv_zusatzbeitrag: percent, e.g. 2.9 (not 0.029).
    'krankenversicherung', 'rentenversicherung' are original PAP codes.
    """
    def cents(v):
        return int((D(str(v)) * 100).quantize(D("1"), rounding=ROUND_DOWN))
    args = dict(RE4=cents(brutto_eur), STKL=int(steuerklasse), LZZ=int(zeitraum),
                KVZ=D(str(kv_zusatzbeitrag)), PVZ=int(pv_kinderlos),
                PVS=int(pv_sachsen), ZKF=D(str(pv_kinder)),
                KRV=int(rentenversicherung), PKV=int(krankenversicherung),
                JFREIB=cents(freibetrag_jahr_eur),
                JHINZU=cents(hinzurechnung_jahr_eur),
                R=int(kirchensteuer))
    args.update(pap_parameter)
    result = pap2026(**args)
    return {key: float(D(value) / 100) for key, value in result.items()}
