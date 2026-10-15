TAB2 = [D("0"), D("3000"), D("2880"), D("2760"), D("2640"), D("2520"), D("2400"), D("2280"), D("2160"), D("2040"), D("1920"), D("1800"), D("1680"), D("1560"), D("1440"), D("1320"), D("1200"), D("1140"), D("1080"), D("1050"), D("1020"), D("990"), D("960"), D("930"), D("900"), D("870"), D("840"), D("810"), D("780"), D("750"), D("720"), D("690"), D("660"), D("630"), D("600"), D("570"), D("540"), D("510"), D("480"), D("450"), D("420"), D("390"), D("360"), D("330"), D("300"), D("270"), D("240"), D("210"), D("180"), D("150"), D("120"), D("90"), D("60"), D("30"), D("0")]
TAB3 = [D("0"), D("900"), D("864"), D("828"), D("792"), D("756"), D("720"), D("684"), D("648"), D("612"), D("576"), D("540"), D("504"), D("468"), D("432"), D("396"), D("360"), D("342"), D("324"), D("315"), D("306"), D("297"), D("288"), D("279"), D("270"), D("261"), D("252"), D("243"), D("234"), D("225"), D("216"), D("207"), D("198"), D("189"), D("180"), D("171"), D("162"), D("153"), D("144"), D("135"), D("126"), D("117"), D("108"), D("99"), D("90"), D("81"), D("72"), D("63"), D("54"), D("45"), D("36"), D("27"), D("18"), D("9"), D("0")]
TAB4 = [D("0"), D("0.4"), D("0.384"), D("0.368"), D("0.352"), D("0.336"), D("0.32"), D("0.304"), D("0.288"), D("0.272"), D("0.256"), D("0.24"), D("0.224"), D("0.208"), D("0.192"), D("0.176"), D("0.16"), D("0.152"), D("0.144"), D("0.14"), D("0.136"), D("0.132"), D("0.128"), D("0.124"), D("0.12"), D("0.116"), D("0.112"), D("0.108"), D("0.104"), D("0.1"), D("0.096"), D("0.092"), D("0.088"), D("0.084"), D("0.08"), D("0.076"), D("0.072"), D("0.068"), D("0.064"), D("0.06"), D("0.056"), D("0.052"), D("0.048"), D("0.044"), D("0.04"), D("0.036"), D("0.032"), D("0.028"), D("0.024"), D("0.02"), D("0.016"), D("0.012"), D("0.008"), D("0.004"), D("0")]
TAB5 = [D("0"), D("1900"), D("1824"), D("1748"), D("1672"), D("1596"), D("1520"), D("1444"), D("1368"), D("1292"), D("1216"), D("1140"), D("1064"), D("988"), D("912"), D("836"), D("760"), D("722"), D("684"), D("665"), D("646"), D("627"), D("608"), D("589"), D("570"), D("551"), D("532"), D("513"), D("494"), D("475"), D("456"), D("437"), D("418"), D("399"), D("380"), D("361"), D("342"), D("323"), D("304"), D("285"), D("266"), D("247"), D("228"), D("209"), D("190"), D("171"), D("152"), D("133"), D("114"), D("95"), D("76"), D("57"), D("38"), D("19"), D("0")]
ZAHL1 = D("1")
ZAHL2 = D("2")
ZAHL5 = D("5")
ZAHL7 = D("7")
ZAHL12 = D("12")
ZAHL100 = D("100")
ZAHL360 = D("360")
ZAHL500 = D("500")
ZAHL700 = D("700")
ZAHL1000 = D("1000")
ZAHL10000 = D("10000")

def MPARA(z: Zustand) -> None:
    z.BBGRVALV = D("101400")
    z.AVSATZAN = D("0.013")
    z.RVSATZAN = D("0.093")
    z.BBGKVPV = D("69750")
    z.KVSATZAN = ((((z.KVZ / ZAHL2) / ZAHL100)) + D("0.07"))
    if (z.PVS == D("1")):
        z.PVSATZAN = D("0.023")
    else:
        z.PVSATZAN = D("0.018")
    if (z.PVZ == D("1")):
        z.PVSATZAN = (z.PVSATZAN + D("0.006"))
    else:
        z.PVSATZAN = (z.PVSATZAN - (z.PVA * D("0.0025")))
    z.W1STKL5 = D("14071")
    z.W2STKL5 = D("34939")
    z.W3STKL5 = D("222260")
    z.GFB = D("12348")
    z.SOLZFREI = D("20350")


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

