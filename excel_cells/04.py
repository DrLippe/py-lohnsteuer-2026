def UPANTEIL(z: Zustand) -> None:
    if (z.LZZ == D("1")):
        z.ANTEIL1 = z.JW
    else:
        if (z.LZZ == D("2")):
            z.ANTEIL1 = teilen(z.JW, ZAHL12, D("0"), 'ROUND_DOWN')
        else:
            if (z.LZZ == D("3")):
                z.ANTEIL1 = teilen(((z.JW * ZAHL7)), ZAHL360, D("0"), 'ROUND_DOWN')
            else:
                z.ANTEIL1 = teilen(z.JW, ZAHL360, D("0"), 'ROUND_DOWN')


def MSONST(z: Zustand) -> None:
    z.LZZ = D("1")
    if (z.ZMVB == D("0")):
        z.ZMVB = D("12")
    if ((vergleiche(z.SONSTB, D("0")) == D("0")) and (vergleiche(z.MBV, D("0")) == D("0"))):
        z.LSTSO = D("0")
        z.STS = D("0")
        z.SOLZS = D("0")
        z.BKS = D("0")
    else:
        MOSONST(z)
        z.ZRE4J = stellen(((((z.JRE4 + z.SONSTB)) / ZAHL100)), D("2"), 'ROUND_DOWN')
        z.ZVBEZJ = stellen(((((z.JVBEZ + z.VBS)) / ZAHL100)), D("2"), 'ROUND_DOWN')
        z.VBEZBSO = z.STERBE
        MRE4SONST(z)
        MLSTJAHR(z)
        z.WVFRBM = stellen((((z.ZVE - z.GFB)) * ZAHL100), D("2"), 'ROUND_DOWN')
        if (vergleiche(z.WVFRBM, D("0")) == (-D("1"))):
            z.WVFRBM = D("0")
        z.LSTSO = (z.ST * ZAHL100)
        z.STS = (teilen(((z.LSTSO - z.LSTOSO) * D(z.f)), ZAHL100, D("0"), 'ROUND_DOWN') * ZAHL100)
        STSMIN(z)


def STSMIN(z: Zustand) -> None:
    if (vergleiche(z.STS, D("0")) == (-D("1"))):
        if (vergleiche(z.MBV, D("0")) == D("0")):
            pass
        else:
            z.LSTLZZ = (z.LSTLZZ + z.STS)
            if (vergleiche(z.LSTLZZ, D("0")) == (-D("1"))):
                z.LSTLZZ = D("0")
            z.SOLZLZZ = stellen((z.SOLZLZZ + (z.STS * (D("5.5") / ZAHL100))), D("0"), 'ROUND_DOWN')
            if (vergleiche(z.SOLZLZZ, D("0")) == (-D("1"))):
                z.SOLZLZZ = D("0")
            z.BK = (z.BK + z.STS)
            if (vergleiche(z.BK, D("0")) == (-D("1"))):
                z.BK = D("0")
        z.STS = D("0")
        z.SOLZS = D("0")
    else:
        MSOLZSTS(z)
    if (z.R > D("0")):
        z.BKS = z.STS
    else:
        z.BKS = D("0")


def MSOLZSTS(z: Zustand) -> None:
    if (vergleiche(z.ZKF, D("0")) == D("1")):
        z.SOLZSZVE = (z.ZVE - z.KFB)
    else:
        z.SOLZSZVE = z.ZVE
    if (vergleiche(z.SOLZSZVE, D("1")) == (-D("1"))):
        z.SOLZSZVE = D("0")
        z.X = D("0")
    else:
        z.X = teilen(z.SOLZSZVE, D(z.KZTAB), D("0"), 'ROUND_DOWN')
    if (z.STKL < D("5")):
        UPTAB26(z)
    else:
        MST5_6(z)
    z.SOLZSBMG = stellen((z.ST * D(z.f)), D("0"), 'ROUND_DOWN')
    if (vergleiche(z.SOLZSBMG, z.SOLZFREI) == D("1")):
        z.SOLZS = teilen((z.STS * D("5.5")), ZAHL100, D("0"), 'ROUND_DOWN')
    else:
        z.SOLZS = D("0")


def MOSONST(z: Zustand) -> None:
    z.ZRE4J = stellen(((z.JRE4 / ZAHL100)), D("2"), 'ROUND_DOWN')
    z.ZVBEZJ = stellen(((z.JVBEZ / ZAHL100)), D("2"), 'ROUND_DOWN')
    z.JLFREIB = teilen(z.JFREIB, ZAHL100, D("2"), 'ROUND_DOWN')
    z.JLHINZU = teilen(z.JHINZU, ZAHL100, D("2"), 'ROUND_DOWN')
    MRE4(z)
    MRE4ABZ(z)
    z.ZRE4VP = (z.ZRE4VP - (z.JRE4ENT / ZAHL100))
    MZTABFB(z)
    z.VFRBS1 = stellen(((((z.ANP + (z.FVB + z.FVBZ))) * ZAHL100)), D("2"), 'ROUND_DOWN')
    MLSTJAHR(z)
    z.WVFRBO = stellen(((((z.ZVE - z.GFB)) * ZAHL100)), D("2"), 'ROUND_DOWN')
    if (vergleiche(z.WVFRBO, D("0")) == (-D("1"))):
        z.WVFRBO = D("0")
    z.LSTOSO = (z.ST * ZAHL100)


def MRE4SONST(z: Zustand) -> None:
    MRE4(z)
    z.FVB = z.FVBSO
    MRE4ABZ(z)
    z.ZRE4VP = (((z.ZRE4VP + (z.MBV / ZAHL100)) - (z.JRE4ENT / ZAHL100)) - (z.SONSTENT / ZAHL100))
    z.FVBZ = z.FVBZSO
    MZTABFB(z)
    z.VFRBS2 = ((((((((z.ANP + z.FVB) + z.FVBZ))) * ZAHL100))) - z.VFRBS1)


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

