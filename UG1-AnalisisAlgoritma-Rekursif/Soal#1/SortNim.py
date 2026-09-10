def InsertRecursive(sorted_array, current_value, current_length):
    if current_length == 0:
        return [current_value]

    ganjil = int(NIM_MAHASISWA[-1]) % 2 == 1

    if (ganjil and current_value < sorted_array[current_length - 1]) or \
       (not ganjil and current_value > sorted_array[current_length - 1]):
        return InsertRecursive(
            sorted_array,
            current_value,
            current_length - 1
        ) + [sorted_array[current_length - 1]]

    return sorted_array[:current_length] + [current_value]


def RecursiveFilterSort(data_array, current_length):
    if current_length == 0:
        return []

    result = RecursiveFilterSort(data_array, current_length - 1)
    current_value = data_array[current_length - 1]

    if current_value % 2 == int(NIM_MAHASISWA[-1]) % 2:
        return InsertRecursive(result, current_value, len(result))

    return result


# Ganti dengan NIM Anda
NIM_MAHASISWA = "71251182"


if NIM_MAHASISWA != "":
    raw_data = [int(digit) for digit in NIM_MAHASISWA]
    data_length = len(raw_data)

    final_result = RecursiveFilterSort(raw_data, data_length)

    print("==== FILTER & SORT NIM ====")
    print("NIM Mahasiswa :", NIM_MAHASISWA)

    if int(NIM_MAHASISWA[-1]) % 2 == 1:
        print("Tipe          : GANJIL (Ascending)")
    else:
        print("Tipe          : GENAP (Descending)")

    print("Data Digit Awal :", raw_data)
    print("Hasil Akhir     :", final_result)