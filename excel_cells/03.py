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


def MZTABFB(z: Zustand) -> None:
    z.ANP = D("0")
    if ((vergleiche(z.ZVBEZ, D("0")) >= D("0")) and (vergleiche(z.ZVBEZ, z.FVBZ) == (-D("1")))):
        z.FVBZ = D(int(z.ZVBEZ))
    if (z.STKL < D("6")):
        if (vergleiche(z.ZVBEZ, D("0")) == D("1")):
            if (vergleiche(((z.ZVBEZ - z.FVBZ)), D("102")) == (-D("1"))):
                z.ANP = stellen(((z.ZVBEZ - z.FVBZ)), D("0"), 'ROUND_UP')
            else:
                z.ANP = D("102")
    else:
        z.FVBZ = D("0")
        z.FVBZSO = D("0")
    if (z.STKL < D("6")):
        if (vergleiche(z.ZRE4, z.ZVBEZ) == D("1")):
            if (vergleiche((z.ZRE4 - z.ZVBEZ), D("1230")) == (-D("1"))):
                z.ANP = stellen(((z.ANP + z.ZRE4) - z.ZVBEZ), D("0"), 'ROUND_UP')
            else:
                z.ANP = (z.ANP + D("1230"))
    z.KZTAB = D("1")
    if (z.STKL == D("1")):
        z.SAP = D("36")
        z.KFB = stellen(((z.ZKF * D("9756"))), D("0"), 'ROUND_DOWN')
    else:
        if (z.STKL == D("2")):
            z.EFA = D("4260")
            z.SAP = D("36")
            z.KFB = stellen(((z.ZKF * D("9756"))), D("0"), 'ROUND_DOWN')
        else:
            if (z.STKL == D("3")):
                z.KZTAB = D("2")
                z.SAP = D("36")
                z.KFB = stellen(((z.ZKF * D("9756"))), D("0"), 'ROUND_DOWN')
            else:
                if (z.STKL == D("4")):
                    z.SAP = D("36")
                    z.KFB = stellen(((z.ZKF * D("4878"))), D("0"), 'ROUND_DOWN')
                else:
                    if (z.STKL == D("5")):
                        z.SAP = D("36")
                        z.KFB = D("0")
                    else:
                        z.KFB = D("0")
    z.ZTABFB = stellen(((((z.EFA + z.ANP) + z.SAP) + z.FVBZ)), D("2"), 'ROUND_DOWN')


def MLSTJAHR(z: Zustand) -> None:
    UPEVP(z)
    z.ZVE = ((z.ZRE4 - z.ZTABFB) - z.VSP)
    UPMLST(z)


def UPLSTLZZ(z: Zustand) -> None:
    z.JW = (z.LSTJAHR * ZAHL100)
    UPANTEIL(z)
    z.LSTLZZ = z.ANTEIL1


def UPMLST(z: Zustand) -> None:
    if (vergleiche(z.ZVE, ZAHL1) == (-D("1"))):
        z.ZVE = D("0")
        z.X = D("0")
    else:
        z.X = stellen(((z.ZVE / D(z.KZTAB))), D("0"), 'ROUND_DOWN')
    if (z.STKL < D("5")):
        UPTAB26(z)
    else:
        MST5_6(z)


def UPEVP(z: Zustand) -> None:
    if (z.KRV == D("1")):
        z.VSPR = D("0")
    else:
        if (vergleiche(z.ZRE4VP, z.BBGRVALV) == D("1")):
            z.ZRE4VPR = z.BBGRVALV
        else:
            z.ZRE4VPR = z.ZRE4VP
        z.VSPR = stellen(((z.ZRE4VPR * z.RVSATZAN)), D("2"), 'ROUND_DOWN')
    MVSPKVPV(z)
    if (z.ALV == D("1")):
        pass
    else:
        if (z.STKL == D("6")):
            pass
        else:
            MVSPHB(z)


def MVSPKVPV(z: Zustand) -> None:
    if (vergleiche(z.ZRE4VP, z.BBGKVPV) == D("1")):
        z.ZRE4VPR = z.BBGKVPV
    else:
        z.ZRE4VPR = z.ZRE4VP
    if (z.PKV > D("0")):
        if (z.STKL == D("6")):
            z.VSPKVPV = D("0")
        else:
            z.PKPVAGZJ = stellen(((z.PKPVAGZ * ZAHL12) / ZAHL100), D("2"), 'ROUND_DOWN')
            z.VSPKVPV = stellen(((z.PKPV * ZAHL12) / ZAHL100), D("2"), 'ROUND_DOWN')
            z.VSPKVPV = (z.VSPKVPV - z.PKPVAGZJ)
            if (vergleiche(z.VSPKVPV, D("0")) == (-D("1"))):
                z.VSPKVPV = D("0")
    else:
        z.VSPKVPV = stellen((z.ZRE4VPR * (z.KVSATZAN + z.PVSATZAN)), D("2"), 'ROUND_DOWN')
    z.VSP = stellen((z.VSPKVPV + z.VSPR), D("0"), 'ROUND_UP')


def MVSPHB(z: Zustand) -> None:
    if (vergleiche(z.ZRE4VP, z.BBGRVALV) == D("1")):
        z.ZRE4VPR = z.BBGRVALV
    else:
        z.ZRE4VPR = z.ZRE4VP
    z.VSPALV = stellen((z.AVSATZAN * z.ZRE4VPR), D("2"), 'ROUND_DOWN')
    z.VSPHB = stellen((z.VSPALV + z.VSPKVPV), D("2"), 'ROUND_DOWN')
    if (vergleiche(z.VSPHB, D("1900")) == D("1")):
        z.VSPHB = D("1900")
    z.VSPN = stellen((z.VSPR + z.VSPHB), D("0"), 'ROUND_UP')
    if (vergleiche(z.VSPN, z.VSP) == D("1")):
        z.VSP = z.VSPN


def MST5_6(z: Zustand) -> None:
    z.ZZX = z.X
    if (vergleiche(z.ZZX, z.W2STKL5) == D("1")):
        z.ZX = z.W2STKL5
        UP5_6(z)
        if (vergleiche(z.ZZX, z.W3STKL5) == D("1")):
            z.ST = stellen(((z.ST + (((z.W3STKL5 - z.W2STKL5)) * D("0.42")))), D("0"), 'ROUND_DOWN')
            z.ST = stellen(((z.ST + (((z.ZZX - z.W3STKL5)) * D("0.45")))), D("0"), 'ROUND_DOWN')
        else:
            z.ST = stellen(((z.ST + (((z.ZZX - z.W2STKL5)) * D("0.42")))), D("0"), 'ROUND_DOWN')
    else:
        z.ZX = z.ZZX
        UP5_6(z)
        if (vergleiche(z.ZZX, z.W1STKL5) == D("1")):
            z.VERGL = z.ST
            z.ZX = z.W1STKL5
            UP5_6(z)
            z.HOCH = stellen(((z.ST + (((z.ZZX - z.W1STKL5)) * D("0.42")))), D("0"), 'ROUND_DOWN')
            if (vergleiche(z.HOCH, z.VERGL) == (-D("1"))):
                z.ST = z.HOCH
            else:
                z.ST = z.VERGL


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

