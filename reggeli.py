vendegek_szama = int(input("Vendégek száma: "))
tojasok_szama = int(input("Raktáron lévő tojások: "))

szugseges = vendegek_szama * 3 * 1.1

if tojasok_szama > szugseges:
    maradek = tojasok_szama - szugseges
    print(f"Ennyi vendéghez {szugseges} tojásra van szügség.")
    print("Elég lesz a tojás.")
    print(f"Maradni fog {maradek} tojás.")
else:
    kell_meg = szugseges - tojasok_szama
    print(f"Ennyi vendéghez {szugseges} tojásra van szügség.")
    print(f"Még kell venni {kell_meg} tojást.")

