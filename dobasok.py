import random

def kozte(szam, also, felso):
    if also <= szam <= felso:
        return True
    else:
        return False

dobasok_szama = 150
talalatok = 0

for _ in range(dobasok_szama):
    dobas = random.randint(1, 12)
    if kozte(dobas, 4, 8):
        talalatok += 1

szazalek = (talalatok / dobasok_szama) * 100

print(f"A {dobasok_szama} dobásból {talalatok} esett 4 és 8 közé.")
print(f"Ez az összes dobás {szazalek:.2f}%-a.")