
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import requests

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
}

st.set_page_config(page_title="Dashboard Katalog Buku", layout="wide")
st.title("Dashboard Katalog Buku")
st.write("Mengambil data buku melalui web scraping dan kurs GBP/IDR melalui REST API.")

jumlah_halaman = st.slider("Jumlah halaman katalog yang diambil", 1, 3, 2)

if st.button("Ambil Data dan Tampilkan Dashboard", type="primary"):

    # Web Scraping
    daftar_buku = []

    with st.spinner("Sedang mengambil data buku..."):
        try:
            for halaman in range(1, jumlah_halaman + 1):
                url = f"https://books.toscrape.com/catalogue/page-{halaman}.html"

                response = requests.get(url, timeout=15)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, "html.parser")

                buku = soup.select("article.product_pod")

                for item in buku:
                    judul = item.h3.a["title"]

                    harga = item.select_one("p.price_color").text
                    harga_gbp = float(
                        harga.replace("£", "").replace("Â", "").strip()
                    )

                    rating_text = item.select_one(
                        "p.star-rating"
                    )["class"][1]

                    rating = RATING_MAP[rating_text]

                    ketersediaan = item.select_one(
                        "p.instock.availability"
                    ).get_text(strip=True)

                    daftar_buku.append({
                        "judul": judul,
                        "harga_gbp": harga_gbp,
                        "rating": rating,
                        "ketersediaan": ketersediaan
                    })

            if not daftar_buku:
                st.warning("Tidak ada data buku yang berhasil diambil.")
                st.stop()

            # REST API Kurs GBP ke IDR
            api_url = "https://api.frankfurter.dev/v1/latest?base=GBP&symbols=IDR"

            api_response = requests.get(api_url, timeout=15)
            api_response.raise_for_status()

            data_kurs = api_response.json()
            kurs = data_kurs["rates"]["IDR"]

            # Pengolahan DataFrame
            df = pd.DataFrame(daftar_buku)

            df["harga_idr"] = df["harga_gbp"] * kurs

            # Menampilkan Data
            st.success(f"Kurs terbaru GBP/IDR: Rp{kurs:,.2f}")

            st.subheader("Data Katalog Buku")
            st.write(
                f"{len(df)} buku diambil dari {jumlah_halaman} halaman."
            )

            st.dataframe(df, use_container_width=True)

            # Visualisasi
            st.subheader("Visualisasi")
            col1, col2 = st.columns(2)

            with col1:
                fig1, ax1 = plt.subplots()

                ax1.hist(df["harga_idr"], bins=10, edgecolor="black")

                ax1.set_title("Distribusi Harga Buku")
                ax1.set_xlabel("Harga (Rupiah)")
                ax1.set_ylabel("Jumlah Buku")

                st.pyplot(fig1)
                plt.close(fig1)

            with col2:
                fig2, ax2 = plt.subplots()

                jumlah_rating = (
                    df["rating"]
                    .value_counts()
                    .reindex([1, 2, 3, 4, 5], fill_value=0)
                )

                ax2.bar(jumlah_rating.index, jumlah_rating.values)

                ax2.set_title("Jumlah Buku Berdasarkan Rating")
                ax2.set_xlabel("Rating")
                ax2.set_ylabel("Jumlah Buku")
                ax2.set_xticks([1, 2, 3, 4, 5])

                st.pyplot(fig2)
                plt.close(fig2)

        except requests.exceptions.RequestException as e:
            st.error(f"Gagal mengambil data dari website atau API: {e}")

        except (KeyError, ValueError, AttributeError) as e:
            st.error(f"Terjadi kesalahan saat mengolah data: {e}")
