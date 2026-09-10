def piramida_angka(angka):
    for i in range(1, angka + 1):
        print(" " *(angka - i) * 2, end=" ")
        for j in range(1, i + 1):
            if j == i:
                print(j, end='')
            else:
                print(j, end=' ')
        for j in range(i-1,0,-1):
            if j == i:
                print(" " + str(j), end="")
            else:
                print(" " + str(j), end="")
        print()
print("Test Case = 1)")
piramida_angka(1)
print("==============================")
print("Test Case = 2)")
piramida_angka(2)
print("==============================")
print("Test Case = 3)")
piramida_angka(3)
print("==============================")
print("Test Case = 4)")
piramida_angka(4)
print("==============================")
print("Test Case = 5)")
piramida_angka(5)
print("==============================")
print("Test Case = 6)")
piramida_angka(6)
print("==============================")
print("Test Case = 7)")
piramida_angka(7)
print("==============================")
print("Test Case = 8)")
piramida_angka(8)
print("==============================")
print("Test Case = 9)")
piramida_angka(9)
print("==============================")