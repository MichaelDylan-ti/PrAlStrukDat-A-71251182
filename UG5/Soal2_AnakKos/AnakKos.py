import streamlit as st
import pandas as pd

# --- Title ---
st.title("Pengeluaran Anak Kos: 71251182")

# --- Input Uang Bulanan ---
st.subheader("Uang Bulanan")
uang_bulanan = st.number_input("Masukkan Uang Bulanan", min_value=0,step=100000)


# --- Input Pengeluaran ---
st.subheader("Pengeluaran Bulanan")
makanan = st.number_input("Pengeluaran Makanan", min_value=0,step=10000) # Ada 5
kos = st.number_input("Pengeluaran Kos",  min_value=0,step=10000) # Kategori
transportasi = st.number_input("Pengeluaran Transportasi", min_value=0,step=10000) # Pengeluaran
internet = st.number_input("Pengeluaran Internet",  min_value=0,step=10000) # Ya kan
hiburan = st.number_input("Pengeluaran Hiburan",  min_value=0,step=10000) # Paham lah ya

# --- Tombol Ngitung Pengeluaran ---
if st.button("Hitung Pengeluaran"):
    st.write("Ringkasan Keuangan")
    # --- Ngitung Total Pengeluaran ---
    total_pengeluaran = (makanan + kos + transportasi + internet + hiburan)

    # --- Ngitung Sisa Uang ---
    sisa_uang = uang_bulanan - total_pengeluaran


    # --- Menampilkan Hasil Perhitungan ---
    st.subheader("Ringkasan Keuangan")
    kolom1, kolom2, kolom3 = st.columns(3)
    with kolom1:
        st.metric(
            # Tampilin uang bulanan di sini
            label = "Uang Bulanan", 
            value = uang_bulanan
        )
    with kolom2:
        st.metric(
            # Tampilin total pengeluaran di sini
            label = "Total Pengeluaran", 
            value = total_pengeluaran
        )
    with kolom3:
        st.metric(
            # Tampilin sisa uang di sini
            label = "Sisa Uang", 
            value = sisa_uang
        )


    # --- Kondisi Keuangan ---
    st.subheader("Kondisi Keuangan")

    # Kondisi 1
    if sisa_uang > 0:
        st.success("Keuanganmu masih aman bulan ini!")

    # Kondisi 2
    elif sisa_uang == 0:
        st.warning("Uangmu habis..")

    # Kondisi 3
    else:
        if sisa_uang < 0:
            st.error("Pengeluaranmu melebihi uang bulanan!")


    # --- Data Pengeluaran ---
    # Ini gausah diubah! 
    # Udah kubantu bikinin, tinggal dipake aja
    data_pengeluaran = {
        "Kategori": [
            "Makanan",
            "Kos",
            "Transportasi",
            "Internet/Pulsa",
            "Hiburan"
        ],
        "Pengeluaran": [
            makanan,
            kos,
            transportasi,
            internet,
            hiburan
        ]
    }

    df_pengeluaran = pd.DataFrame(data_pengeluaran)

    # --- Pengeluaran Terbesar ---
    pengeluaran_terbesar = [] # Cari pengeluaran terbesar

    nilai_terbesar = max(
            makanan,
            kos,
            transportasi,
            internet,
            hiburan
        )
    if makanan == nilai_terbesar:
        pengeluaran_terbesar.append("makanan")
    if kos == nilai_terbesar:
        pengeluaran_terbesar.append("kos")
    if transportasi == nilai_terbesar:
        pengeluaran_terbesar.append("transportasi")
    if internet == nilai_terbesar:
        pengeluaran_terbesar.append("internet")
    if hiburan == nilai_terbesar:
        pengeluaran_terbesar.append("hiburan")
    
    st.subheader("Pengeluaran Terbesar")
    st.write(pengeluaran_terbesar[0]) # Tampilin pengeluaran terbesar di sini

    # --- Grafik Pengeluaran ---
    st.subheader("Grafik Pengeluaran")
    st.bar_chart(df_pengeluaran.set_index("Kategori"))# Tampilin grafik pengeluaran di sini