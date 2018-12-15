print("umowa o pracę: a")
print("umowa zlecenie: b")

a = input("Wybierz wariant kalkulacji aby kontynuować: ")

if a.lower() == "a":
    aWynagrodzenieBrutto = round(float(input("Podaj kwotę wynagrodznia brutto: ")), 2)
    print("""Przykładowa wypłata pracownika zostanie obliczona przy założeniach, że:
\t - pracownikowi przysługują podstawowe koszty uzyskania przychodu, tj. 111,25 zł,
\t - zaliczka na PIT zostaje co miesiąc pomniejszona o 1/12 kwoty zmniejszającej podatek dochodowy, tj. o 46,33 zł,
\t - pracownik jest zatrudniony w firmie, dla której stopa procentowa składki wypadkowej wynosi 1,8%.""")


    print("\na | wynagrodzenie brutto będące podstawą wymiaru składek:", aWynagrodzenieBrutto)


    bEmerytalna = aWynagrodzenieBrutto*0.0976
    bRentowa = aWynagrodzenieBrutto*0.015
    bChorobowa = aWynagrodzenieBrutto*0.0245
    b = round((bEmerytalna+bRentowa+bChorobowa), 2)
    print("b | składki finansowane przez pracownika:", b, "zł")
    print("\t - emerytalna 9,76% x a =", round(bEmerytalna, 2), "zł")
    print("\t - rentowa 1,5% x a = ", round(bRentowa, 2))
    print("\t - chorobowa 2,45% x a =", round(bChorobowa, 2), "zł")

    c = aWynagrodzenieBrutto - b
    print("c | podstawa wymiaru składki zdrowotnej a - b:", round(c, 2), "zł")

    d = round(c*0.09, 2)
    print("d | składka zdrowotna do zapłaty 9% x c:", d, "zł")

    e = c*0.0775
    print("e | składka zdrowotna do odliczenia od podatku 7,75% x c:", round(e, 2), "zł")

    f = 111.25
    print("f | koszty uzyskania przychodu:", f, "zł")

    g = round(aWynagrodzenieBrutto - f - b)
    print("g | podstawa obliczenia zaliczki na PIT (zaokrąglamy do pełnych złotych) a - f - b:", g, "zł")

    h = round(g*0.18 - 46.33 - e)
    print("h | zaliczka na PIT (zaokrąglamy do pełnych złotych) (18% x g) - 46,33 zł - e:", h, "zł")

    i = round(aWynagrodzenieBrutto - b - d - h, 2)
    print("i | wynagrodzenie netto do wypłaty a - b - d - h:", i)



elif a.lower() == "b":
    kwotaUmowaZlecenie = round(float(input("Podaj kwotę umowy zlecenia: ")), 2)
    if(kwotaUmowaZlecenie <= 200):
        skladka_2 = round(kwotaUmowaZlecenie*0.1371, 2)
        podstawaWymiaru_3 = round(kwotaUmowaZlecenie - skladka_2, 2)
        skladka_4 = round(podstawaWymiaru_3*0.09, 2)
        podstawaOpodatkowania_5 = round(kwotaUmowaZlecenie)
        podatekRyczalt_6 = round(kwotaUmowaZlecenie*0.18)
        doWyplaty_7 = kwotaUmowaZlecenie -(skladka_2 + skladka_4 + podatekRyczalt_6)
        print("Obciążenia podatkowo-składkowe:")
        print("\t1) podstawa wymiaru składek na ubezpieczenia społeczne", kwotaUmowaZlecenie, "zł")
        print("\t2) składki na ubezpieczenia społeczne finansowane przez zleceniobiorcę", skladka_2, "zł")
        print("\t3) podstawa wymiaru składki na ubezpieczenie zdrowotne", podstawaWymiaru_3, "zł")
        print("\t4) składka na ubezpieczenie zdrowotne", skladka_4, "zł")
        print("\t5) podstawa opodatkowania, po zaokrągleniu do pełnych złotych", podstawaOpodatkowania_5, "zł")
        print("\t6) zryczałtowany podatek dochodowy, po zaokrągleniu do pełnych złotych", podatekRyczalt_6, "zł")
        print("\t7) do wypłaty zleceniobiorcy", doWyplaty_7, "zł")
    else:
        skladka_2 = round(kwotaUmowaZlecenie*0.1371, 2)
        podstawaWymiaru_3 = round(kwotaUmowaZlecenie - skladka_2, 2)
        skladka_4_1 = round(podstawaWymiaru_3*0.09, 2)
        skladka_4_2 = round(podstawaWymiaru_3*0.0775, 2)
        kosztyUzyskania_5 = round((kwotaUmowaZlecenie-skladka_2)*0.2, 2)
        podstawaOpodatkowania_6 = round(kwotaUmowaZlecenie - (kosztyUzyskania_5 + skladka_2))
        zaliczkaPodatek_7 = round(podstawaOpodatkowania_6 * 0.18, 2)
        zalPodatekUS_8 = round(zaliczkaPodatek_7 - skladka_4_2)
        doWyplaty_9 = kwotaUmowaZlecenie - (skladka_2 + skladka_4_1 + zalPodatekUS_8)
        print("Obciążenia podatkowo-składkowe:")
        print("\t1) podstawa wymiaru składek na ubezpieczenia społeczne", kwotaUmowaZlecenie, "zł")
        print("\t2) składki na ubezpieczenia społeczne finansowane przez zleceniobiorcę", skladka_2, "zł")
        print("\t3) podstawa wymiaru składki na ubezpieczenie zdrowotne", podstawaWymiaru_3, "zł")
        print("\t4) składka na ubezpieczenie zdrowotne:")
        print("\t\t - 9%\t", skladka_4_1, "zł")
        print("\t\t - 7,75%\t", skladka_4_2, "zł")
        print("\t5) koszty uzyskania przychodów", kosztyUzyskania_5, "zł")
        print("\t6) podstawa opodatkowania, po zaokrągleniu do pełnych złotych", podstawaOpodatkowania_6, "zł")
        print("\t7) zaliczka na podatek", zaliczkaPodatek_7, "zł")
        print("\t8) zaliczka na podatek do przekazania do US, po zaokrągleniu do pełnych złotych", zalPodatekUS_8, "zł")
        print("\t9) do wypłaty zleceniobiorcy", round(doWyplaty_9, 2), "zł")
else:
    print("Wybierz prawidłową opcję.")
