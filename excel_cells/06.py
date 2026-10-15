def UP5_6(z: Zustand) -> None:
    z.X = stellen(((z.ZX * D("1.25"))), D("0"), 'ROUND_DOWN')
    UPTAB26(z)
    z.ST1 = z.ST
    z.X = stellen(((z.ZX * D("0.75"))), D("0"), 'ROUND_DOWN')
    UPTAB26(z)
    z.ST2 = z.ST
    z.DIFF = (((z.ST1 - z.ST2)) * ZAHL2)
    z.MIST = stellen(((z.ZX * D("0.14"))), D("0"), 'ROUND_DOWN')
    if (vergleiche(z.MIST, z.DIFF) == D("1")):
        z.ST = z.MIST
    else:
        z.ST = z.DIFF


def MSOLZ(z: Zustand) -> None:
    z.SOLZFREI = ((z.SOLZFREI * D(z.KZTAB)))
    if (vergleiche(z.JBMG, z.SOLZFREI) == D("1")):
        z.SOLZJ = stellen((((z.JBMG * D("5.5"))) / ZAHL100), D("2"), 'ROUND_DOWN')
        z.SOLZMIN = stellen(((((z.JBMG - z.SOLZFREI)) * D("11.9")) / ZAHL100), D("2"), 'ROUND_DOWN')
        if (vergleiche(z.SOLZMIN, z.SOLZJ) == (-D("1"))):
            z.SOLZJ = z.SOLZMIN
        z.JW = stellen((z.SOLZJ * ZAHL100), D("0"), 'ROUND_DOWN')
        UPANTEIL(z)
        z.SOLZLZZ = z.ANTEIL1
    else:
        z.SOLZLZZ = D("0")
    if (z.R > D("0")):
        z.JW = (z.JBMG * ZAHL100)
        UPANTEIL(z)
        z.BK = z.ANTEIL1
    else:
        z.BK = D("0")


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

