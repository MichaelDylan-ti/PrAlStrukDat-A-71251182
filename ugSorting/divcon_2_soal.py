# Data mahasiswa dan 5 nilai UG
mahasiswa = [
    {"nama": "Andi", "nilai": [80, 75, 90, 70, 85]},
    {"nama": "Budi", "nilai": [60, 65, 70, 55, 60]},
    {"nama": "Citra", "nilai": [90, 85, 95, 88, 92]},
    {"nama": "Deni", "nilai": [70, 75, 65, 72, 68]},
    {"nama": "Eka", "nilai": [85, 80, 78, 90, 87]},
    {"nama": "Fajar", "nilai": [65, 70, 68, 60, 72]},
    {"nama": "Gina", "nilai": [88, 92, 85, 90, 87]},
    {"nama": "Hadi", "nilai": [75, 80, 70, 78, 72]},
    {"nama": "Intan", "nilai": [55, 60, 65, 58, 62]},
    {"nama": "Joko", "nilai": [78, 82, 75, 80, 85]}
]


# Menghitung rata-rata nilai setiap mahasiswa
for rata2_mahasiswa in mahasiswa:
    rata2_mahasiswa["rata-rata"] = sum(rata2_mahasiswa["nilai"]) / len(rata2_mahasiswa["nilai"])


# Divide and Conquer - Merge Sort
def merge_sort(data):
    if len(data) <= 1:
        return data

    tengah = len(data) // 2
    kiri = data[:tengah]
    kanan = data[tengah:]

    kiri = merge_sort(kiri)
    kanan = merge_sort(kanan)

    return merge(kiri, kanan)


def merge(kiri, kanan):
    result = []
    i = 0
    j = 0
    while i < len(kiri) and j < len(kanan):
        if kiri[i]["rata-rata"] >= kanan[j]["rata-rata"]:
            result.append(kiri[i])
            i += 1
        else:
            result.append(kanan[j])
            j += 1

    while i < len(kiri):
        result.append(kiri[i])
        i += 1
    while j < len(kanan):
        result.append(kanan[j])
        j += 1

    return result


# Menghitung rata-rata keseluruhan)
total_rata2 = 0
for rata2_mahasiswa in mahasiswa:
    total_rata2 += rata2_mahasiswa["rata-rata"]
hasil_rata2 = total_rata2 / len(mahasiswa)


# Mengurutkan mahasiswa menggunakan Merge Sort
mahasiswa_urut = merge_sort(mahasiswa)
atas = []
bawah = []

for rata2_mahasiswa in mahasiswa_urut:
    if rata2_mahasiswa["rata-rata"] >= hasil_rata2:
        atas.append(rata2_mahasiswa)
    else:
        bawah.append(rata2_mahasiswa)

# Menampilkan hasil rata-rata keseluruhan
print("rata-rata keseluruhan: ", hasil_rata2)

print("\n=== DI ATAS / SAMA DENGAN RATA-RATA ===")
# Tampilkan List di atas / sama dengan rata-rata
angka = 1
for rata2_mahasiswa in atas:
    print(
        angka,
        ".",
        rata2_mahasiswa["nama"],
        "- Nilai:",
        rata2_mahasiswa["nilai"],
        "- Rata-rata",
        rata2_mahasiswa["rata-rata"]
    )
    angka += 1

print("\n=== DI BAWAH RATA-RATA ===")
# Tampilkan List di bawah rata-rata
angka = 1
for rata2_mahasiswa in bawah:
    print(
        angka,
        ".",
        rata2_mahasiswa["nama"],
        "- Nilai:",
        rata2_mahasiswa["nilai"],
        "- Rata-rata",
        rata2_mahasiswa["rata-rata"]
    )
    angka += 1