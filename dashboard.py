import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


def countperseason(day_df):
    # Mengagregasi data untuk mendapatkan total 'cnt' per 'season' dan menyimpan hasilnya
    season_totals = day_df.groupby('season')['cnt'].sum().reset_index()

    # Membuat bar chart menggunakan hasil agregasi
    plt.figure(figsize=(8, 6)) # Menyesuaikan ukuran figure
    plt.bar(x=season_totals['season'], height=season_totals['cnt'])
    
    # Menambahkan label untuk sumbu x dan y, serta judul
    plt.xlabel('Season')
    plt.ylabel('Jumlah Penyewaan')
    plt.title('Jumlah Penyewaan Sepeda Berdasarkan Musim')

    # Menyimpan visualisasi sebagai file gambar png
    plt.savefig('barchart.png')
    plt.close() # Penting untuk menutup plot agar tidak ditampilkan dua kali di Streamlit

    # Menampilkan gambar di dashboard Streamlit
    st.image('barchart.png')

    st.write(
        """Berdasarkan visualisasi data tersebut, dapat disimpulkan bahwa musim dengan jumlah penyewaan sepeda tertinggi adalah musim Fall, yang menunjukkan bahwa pada musim tersebut merupakan waktu paling populer untuk penyewaan sepeda."""
    )


def countpermonth(day_df):
    plt.figure(figsize=(10, 6))

    # Membuat clustered bar chart
    sns.barplot(data=day_df, x='mnth', y='cnt', hue='yr', errorbar=None)

    # Menambahkan label untuk sumbu x dan y
    plt.xlabel("Bulan")
    plt.ylabel("Jumlah Penyewaan Sepeda")

    # Menambahkan judul
    plt.title("Perbandingan Jumlah Penyewaan Sepeda Per Bulan Pada Tahun 2011 dan 2012")

    # Mengganti label legenda
    plt.legend(title='Tahun', labels=['2011', '2012'])

    # Menyimpan visualisasi sebagai file gambar png
    plt.savefig('clusteredbarchart.png')
    # Menampilkan gambar di dashboard Streamlit
    st.image('clusteredbarchart.png')

    st.write(
        """Berdasarkan visualisasi data tersebut, dapat disimpulkan bahwa perbandingan jumlah penyewaan sepeda tiap bulannya pada tahun 2011 dan 2012 terlihat berbeda. Pada tahun 2012 terjadi kenaikan jumlah penyewa pada setiap bulannya, jika dibandingkan dengan tahun 2011. Namun, distribusi data nya dalam rentang satu tahun masih relatif sama, yaitu terjadi kenaikan pada pertengahan tahun. Apabila diperhatikan dengan seksama, data pada tahun 2011 cenderung hampir membentuk normal distribution.
        """
    )

def main():

    st.title('Hasil Analisis Data Bike Sharing')
    st.header('Pada musim apa yang memiliki jumlah penyewaan sepeda terbanyak?')

    day_df = pd.read_csv('all_data.csv')

    countperseason(day_df)
    st.header('Bagaimana jumlah penyewaan sepeda setiap bulannya pada tahun 2011 dan 2012?')
    countpermonth(day_df)

main()