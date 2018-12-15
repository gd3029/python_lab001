# zadanie 5
import math
a = int(input("Podaj iczbę a: "))
b = int(input("Podaj iczbę b: "))
c = int(input("Podaj iczbę c: "))
print("y =",a,"x^2 +",b,"x +",c)
delta = b**2 - 4*a*c

print("Delta wynosi:",delta)
if(delta < 0):
    print("Jest mniejsza od 0")
    print("Równanie kwadratowe nie posiada rozwiązań w zbiorze liczb rzeczywistych.")
elif(delta == 0):
    print("Jest równa 0")
    print("Równanie kwadratowe posiada jedno rozwiązanie (x = x1 = x2).")
    x = -b / (2*a)
    print("x =", x)
else:
    print("Jest większa od 0")
    print("Równanie kwadratowe posiada dwa rozwiązania x1, x2.")
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print("x1 =", round(x1,4), "x2 =", round(x2, 4))

