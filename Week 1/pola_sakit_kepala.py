def pola_sakit_kepala(panjang, lebar):
    panjang = abs(panjang)
    lebar = abs(lebar)

    if panjang != lebar:
        print("Panjang dan lebar harus sama!!")
        return

    if panjang % 2 == 0 or lebar % 2 == 0:
        print("Panjang dan lebar harus bilangan ganjil!!")
        return
    
    tengah = panjang // 2

    for a in range(panjang):
        for b in range(lebar):
            nomor = (abs(a - tengah) + abs(b - tengah)) + 1
        if b == lebar - 1:
            print(nomor, end="")
        else:
            print(nomor, end=" ")


print("no 1. (pola 7,7)")
pola_sakit_kepala(7, 7)
print()
print("no 2. (Pola 4, 4)")
pola_sakit_kepala(4, 4)
print()
print("no 3. (Pola -15, 15)")
pola_sakit_kepala(-15, 15)