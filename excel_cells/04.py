def MRE4JL(z: Zustand) -> None:
    if (z.LZZ == D("1")):
        z.ZRE4J = teilen(z.RE4, ZAHL100, D("2"), 'ROUND_DOWN')
        z.ZVBEZJ = teilen(z.VBEZ, ZAHL100, D("2"), 'ROUND_DOWN')
        z.JLFREIB = teilen(z.LZZFREIB, ZAHL100, D("2"), 'ROUND_DOWN')
        z.JLHINZU = teilen(z.LZZHINZU, ZAHL100, D("2"), 'ROUND_DOWN')
    else:
        if (z.LZZ == D("2")):
            z.ZRE4J = teilen(((z.RE4 * ZAHL12)), ZAHL100, D("2"), 'ROUND_DOWN')
            z.ZVBEZJ = teilen(((z.VBEZ * ZAHL12)), ZAHL100, D("2"), 'ROUND_DOWN')
            z.JLFREIB = teilen(((z.LZZFREIB * ZAHL12)), ZAHL100, D("2"), 'ROUND_DOWN')
            z.JLHINZU = teilen(((z.LZZHINZU * ZAHL12)), ZAHL100, D("2"), 'ROUND_DOWN')
        else:
            if (z.LZZ == D("3")):
                z.ZRE4J = teilen(((z.RE4 * ZAHL360)), ZAHL700, D("2"), 'ROUND_DOWN')
                z.ZVBEZJ = teilen(((z.VBEZ * ZAHL360)), ZAHL700, D("2"), 'ROUND_DOWN')
                z.JLFREIB = teilen(((z.LZZFREIB * ZAHL360)), ZAHL700, D("2"), 'ROUND_DOWN')
                z.JLHINZU = teilen(((z.LZZHINZU * ZAHL360)), ZAHL700, D("2"), 'ROUND_DOWN')
            else:
                z.ZRE4J = teilen(((z.RE4 * ZAHL360)), ZAHL100, D("2"), 'ROUND_DOWN')
                z.ZVBEZJ = teilen(((z.VBEZ * ZAHL360)), ZAHL100, D("2"), 'ROUND_DOWN')
                z.JLFREIB = teilen(((z.LZZFREIB * ZAHL360)), ZAHL100, D("2"), 'ROUND_DOWN')
                z.JLHINZU = teilen(((z.LZZHINZU * ZAHL360)), ZAHL100, D("2"), 'ROUND_DOWN')
    if (z.af == D("0")):
        z.f = D("1")


def MRE4(z: Zustand) -> None:
    if (vergleiche(z.ZVBEZJ, D("0")) == D("0")):
        z.FVBZ = D("0")
        z.FVB = D("0")
        z.FVBZSO = D("0")
        z.FVBSO = D("0")
    else:
        if (z.VJAHR < D("2006")):
            z.J = D("1")
        else:
            if (z.VJAHR < D("2058")):
                z.J = (z.VJAHR - D("2004"))
            else:
                z.J = D("54")
        if (z.LZZ == D("1")):
            z.VBEZB = (((z.VBEZM * D(z.ZMVB))) + z.VBEZS)
            z.HFVB = stellen(((TAB2[int(z.J)] / ZAHL12) * D(z.ZMVB)), D("0"), 'ROUND_UP')
            z.FVBZ = stellen(((TAB3[int(z.J)] / ZAHL12) * D(z.ZMVB)), D("0"), 'ROUND_UP')
        else:
            z.VBEZB = stellen(((((z.VBEZM * ZAHL12)) + z.VBEZS)), D("2"), 'ROUND_DOWN')
            z.HFVB = TAB2[int(z.J)]
            z.FVBZ = TAB3[int(z.J)]
        z.FVB = stellen(((((z.VBEZB * TAB1[int(z.J)]))) / ZAHL100), D("2"), 'ROUND_UP')
        if (vergleiche(z.FVB, z.HFVB) == D("1")):
            z.FVB = z.HFVB
        if (vergleiche(z.FVB, z.ZVBEZJ) == D("1")):
            z.FVB = z.ZVBEZJ
        z.FVBSO = stellen(((z.FVB + (((z.VBEZBSO * TAB1[int(z.J)])) / ZAHL100))), D("2"), 'ROUND_UP')
        if (vergleiche(z.FVBSO, TAB2[int(z.J)]) == D("1")):
            z.FVBSO = TAB2[int(z.J)]
        z.HFVBZSO = stellen(((((((z.VBEZB + z.VBEZBSO)) / ZAHL100)) - z.FVBSO)), D("2"), 'ROUND_DOWN')
        z.FVBZSO = stellen(((z.FVBZ + ((z.VBEZBSO) / ZAHL100))), D("0"), 'ROUND_UP')
        if (vergleiche(z.FVBZSO, z.HFVBZSO) == D("1")):
            z.FVBZSO = stellen(z.HFVBZSO, D("0"), 'ROUND_UP')
        if (vergleiche(z.FVBZSO, TAB3[int(z.J)]) == D("1")):
            z.FVBZSO = TAB3[int(z.J)]
        z.HFVBZ = stellen(((((z.VBEZB / ZAHL100)) - z.FVB)), D("2"), 'ROUND_DOWN')
        if (vergleiche(z.FVBZ, z.HFVBZ) == D("1")):
            z.FVBZ = stellen(z.HFVBZ, D("0"), 'ROUND_UP')
    MRE4ALTE(z)


def MRE4ALTE(z: Zustand) -> None:
    if (z.ALTER1 == D("0")):
        z.ALTE = D("0")
    else:
        if (z.AJAHR < D("2006")):
            z.K = D("1")
        else:
            if (z.AJAHR < D("2058")):
                z.K = (z.AJAHR - D("2004"))
            else:
                z.K = D("54")
        z.BMG = (z.ZRE4J - z.ZVBEZJ)
        z.ALTE = stellen(((z.BMG * TAB4[int(z.K)])), D("0"), 'ROUND_UP')
        z.HBALTE = TAB5[int(z.K)]
        if (vergleiche(z.ALTE, z.HBALTE) == D("1")):
            z.ALTE = z.HBALTE


def MRE4ABZ(z: Zustand) -> None:
    z.ZRE4 = stellen((((((z.ZRE4J - z.FVB) - z.ALTE) - z.JLFREIB) + z.JLHINZU)), D("2"), 'ROUND_DOWN')
    if (vergleiche(z.ZRE4, D("0")) == (-D("1"))):
        z.ZRE4 = D("0")
    z.ZRE4VP = z.ZRE4J
    z.ZVBEZ = stellen((z.ZVBEZJ - z.FVB), D("2"), 'ROUND_DOWN')
    if (vergleiche(z.ZVBEZ, D("0")) == (-D("1"))):
        z.ZVBEZ = D("0")


def MBERECH(z: Zustand) -> None:
    MZTABFB(z)
    z.VFRB = stellen(((((z.ANP + (z.FVB + z.FVBZ))) * ZAHL100)), D("0"), 'ROUND_DOWN')
    MLSTJAHR(z)
    z.WVFRB = stellen(((((z.ZVE - z.GFB)) * ZAHL100)), D("0"), 'ROUND_DOWN')
    if (vergleiche(z.WVFRB, D("0")) == (-D("1"))):
        z.WVFRB = D("0")
    z.LSTJAHR = stellen(((z.ST * D(z.f))), D("0"), 'ROUND_DOWN')
    UPLSTLZZ(z)
    if (vergleiche(z.ZKF, D("0")) == D("1")):
        z.ZTABFB = (z.ZTABFB + z.KFB)
        MRE4ABZ(z)
        MLSTJAHR(z)
        z.JBMG = stellen(((z.ST * D(z.f))), D("0"), 'ROUND_DOWN')
    else:
        z.JBMG = z.LSTJAHR
    MSOLZ(z)

