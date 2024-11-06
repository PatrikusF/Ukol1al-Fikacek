# Vytvořte pole, které bude mít 5 stringových hodnot.

pole = ["lesy", "mraky", "obloha", "vzduch", "měsíc"]


# Přidejte pomocí metody append() jeden prvek. - "vítr".

pole.append("vítr")
print(pole)

# Odstraňte pomocí metody remove() druhý prvek z pole.

pole.remove("mraky")
print(pole)

#  Zaměňte 5 hodnotu z pole za: "slunce".

pole[4] = "slunce"
print(pole)

#Přidejte 2 stringové hodnoty pole pomocí metody extend().

pole.extend(["horko", "chlad"])
print(pole)

# Vypište základní vytvořené pole a potom každé pole, ve kterém uděláte změnu.

pole = ["lesy", "mraky", "obloha", "vzduch", "měsíc"]
print("základní pole:", pole)

pole[0] = "hory"
print("Změna prvního prvku:", pole)

pole[1] = "déšť"
print("Změna druhého prvku:", pole)

pole.append("sluníčko")
print("Nový prvek na konci:", pole)

pole[-2:] = ["sníh", "voda"]
print("Změna posledních dvou prvků:", pole)

pole.remove("déšť")
print("Po odstranění 'déšť':", pole)