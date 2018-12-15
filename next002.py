wzrost = round(float(input("Podaj swój wzrost w cm: ")))/100
while(wzrost <= 0):
    print("błąd - wzrost nie może być mniejszy równy 0")
    wzrost = round(float(input("Podaj swój wzrost w cm: ")))/100

masa = round(float(input("Podaj swoją wagę w kg: ")), 2)
while(masa <= 0):
    print("błąd - waga nie może być mniejsza równa 0")
    masa = round(float(input("Podaj swoją wagę w kg: ")), 2)

bmi = round(masa / (wzrost*wzrost),1)
print("Twoje BMI =", bmi)

if(bmi < 18.5):
    print("Niedowaga")
elif((bmi>=18.8) & (bmi<25)):
    print("Norma")
elif(bmi >= 25):
    print("Nadwaga")
    if((bmi >= 25) & (bmi<30)):
        print("Okres przed otyłością")
    elif((bmi >= 30) & (bmi < 35)):
        print("Pierwszy stopień otyłości")
    elif((bmi >= 35) & (bmi < 40)):
        print("Drugi stopień otyłości")
    else:
        print("Trzeci stopień otyłości")
