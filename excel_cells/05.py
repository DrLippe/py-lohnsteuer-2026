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
