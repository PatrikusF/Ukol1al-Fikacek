#(začátek jednorozměrného pole) 9 náhodných číselných hodnot 0-100

pole = [10, 55, 48, 5, 1, 3, 90, 8, 18]
print(pole)

#první, peostřední a poslední hodnota pole

a = pole[0]
print(a)
b = pole[4]
print(b)
c = pole[8]
print(c)

#změna indexového pole 5 na číslo 34

print(pole[0])
pole[6]=34
print(pole[6])

#indexově vypsaná 7 hodnota z pole

x = pole [6]
print(x)

#délka pole

y = len(pole)
print(y)

#minimální a maximální hodnota pole

print (min(pole))
print (max(pole))

#----------------------------------------------------------------------------
#druhé pole s libovolnými čísly a libovolnou délkou
import random

pole02 = [1, 30, 58, 96, 43, 100, 89, 12, 24]
print(pole02)

#sčítání a vypisování pole

print(sum(pole+pole02))
print(len(pole+pole02))

#sčítání 1 a 5 hodnoty z pole (indexově)

f = 1
g = 100
print(f + g)

#BONUS - zamíchat pole 
import random

# Vytvoření pole s čísly od 1 do 23
pole = list(range(1, 24))

# Zamíchání pole
random.shuffle(pole)

# Výpis zamíchaného pole
print(pole)
