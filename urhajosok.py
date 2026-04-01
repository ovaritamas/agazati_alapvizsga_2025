class Urhajos:
    def __init__(self, sor):
        adatok = sor.strip().split(';')
        self.nev = adatok[0]
        self.orszag = adatok[1]
        self.nem = adatok[2]
        self.szulev = int(adatok[3])
        self.urido = int(adatok[4])

    def __str__(self):
        return f"""
            Neve: {self.nev}
            Országa: {self.orszag}
            Neme: {self.nem}
            Születési éve: {self.szulev}
            Űrben töltött ideje: {self.urido} nap
        """

# 3.2. és 3.3. feladat
urhajosok = []
with open("02_Python/urhajos.txt", "r", encoding="utf-8") as f:
    fejlec = f.readline()
    for sor in f:
        urhajosok.append(Urhajos(sor))

# 3.4. feladat
print(f"3.4. feladat: Az állományban {len(urhajosok)} űrhajós adatai találhatók.")

# 3.5. feladat
van_olasz = any(u.orszag == "ITA" for u in urhajosok)
olasz_szoveg = "van" if van_olasz else "nincs"
print(f"3.5. feladat: Az űrhajósok között {olasz_szoveg} olasz származású.")

# 3.6. feladat
noi_idok = [u.urido for u in urhajosok if u.nem == "N"]
if noi_idok:
    atlag = sum(noi_idok) / len(noi_idok)
    print(f"3.6. feladat: A női űrhajósok átlagosan {atlag:.2f} napot töltöttek az űrben.")
else:
    print("3.6. feladat: Nincs női űrhajós az állományban.")

# 3.7. feladat
legfiatalabb = urhajosok[0]
for u in urhajosok:
    if u.szulev > legfiatalabb.szulev:
        legfiatalabb = u
print(f"3.7. feladat: A legfiatalabb űrhajós: {legfiatalabb}")
