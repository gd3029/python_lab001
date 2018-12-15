dystans = float(input("Podaj ilość przejechanych kilometrów: "))
paliwo = float(input("Podaj ilość zatankowanych litrów paliwa: "))

while(dystans <= 0 or paliwo <= 0):
    if(dystans <= 0):
        print("dystans nie może być mniejszy równy 0")
        dystans = float(input("Podaj ilość przejechanych kilometrów: "))
    if(paliwo <= 0):
        print("paliwo nie może być mniejsze równe 0")
        paliwo = float(input("Podaj ilość zatankowanych litrów paliwa: "))

srednieSpalanie = (paliwo / dystans)*100

print("Średnie spalanie na 100km wynosi: ", round(srednieSpalanie, 1))

