import random
from dataMahasiswa import data
from fungsiMahasiswa import show_data, presensi_dummy, acak_data

data = data.copy()
presensi_dummy(data)
acak_data(data)



def sort_by(data: list=data, index: str="nim",rev = False):
    maps = {
        "nim":0,
        "nama":1,
        "presensi":2,
    }
    
    kolom = maps[index]

    #Selection Sort
    for i in range(len(data)):
        posisi = i
        for j in range(i + 1, len(data)):
            if rev == False:
                if data[j][kolom] < data[posisi][kolom]:
                    posisi = j
            else:
                if data[j][kolom] > data[posisi][kolom]:
                    posisi = j
        data[i], data[posisi] = data[posisi], data[i]
    
    # Jangan Dihapus
    show_data(data)

sort_by(data)


    
