import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')
st.set_page_config(page_title="Bike Sharing Dataset Analysis")

df = pd.read_csv('dashboard\day.csv')

# Sidebar
st.sidebar.title("Bike Sharing Dataset Analysis")
visualization = st.sidebar.selectbox("Pilih Pertanyaan:", ("Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3", "Pertanyaan 4"))
st.sidebar.caption("Name : Riyaldi Hasan Setiawan")
st.sidebar.caption("E-mail : riy.2923@gmail.com")
st.sidebar.caption("ID Dicoding : Riyaldi Hasan Setiawan")
st.sidebar.caption('Copyright (c) Riyaldi Hasan Setiawan 2024')


# Main
st.header("Bike Sharing Dataset Analysis")
st.caption("")

if visualization == "Pertanyaan 1":
    st.subheader("Bagaimana pengaruh musim terhadap jumlah total transaksi bike sharing?")

    season_year_cnt = df.groupby(['season', 'yr'])['cnt'].sum().unstack()
    season_year_cnt.plot(kind='line', figsize=(10, 6))

    plt.title('Jumlah Total Transaksi Bike Sharing per Musim (Tahun 2011 & 2012)')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Total Transaksi')
    plt.xticks([1, 2, 3, 4], ['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
    plt.legend(['2011', '2012'])
    st.pyplot(plt)

    st.caption("Dari data 2 tahun di atas musim berpengaruh terhadap jumlah transaksi, tren untuk tahun 2011 sama dengan tren tahun 2012 dimana musim paling banyak transaksi peminjaman terjadi pada musim gugur diikuti musim panas, musim dingin, lalu musim semi.")

elif visualization == "Pertanyaan 2":
    st.subheader("Apakah ada perbedaan signifikan dalam jumlah transaksi bike sharing antara hari libur dan hari kerja?")

    workingday_group = {
        0: 'Bukan hari kerja',
        1: 'Hari kerja'
    }
    df['workingday_group'] = df['workingday'].map(workingday_group)

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='workingday_group', y='cnt', data=df)
    plt.title('Distribusi transaksi peminjaman saat hari kerja vs bukan hari kerja')
    plt.xlabel('Hari kerja')
    plt.ylabel('Jumlah transaksi peminjaman')
    st.pyplot(plt)

    st.caption("Tidak ada perbedaan signifikan dalam jumlah transaksi bike sharing antara hari libur dan hari kerja jika dilihat distribusi data transaksi.")

elif visualization == "Pertanyaan 3":
    st.subheader("Bagaimana cuaca mempengaruhi jumlah pengguna casual dan registered?")

    weather_group = {
        1: 'Cerah',
        2: 'Berkabut',
        3: 'Salju Ringan/Hujan Ringan',
        4: 'Hujan Lebat/Badai Salju'
    }
    df['weather_group'] = df['weathersit'].map(weather_group);

    weather_analysis = df.groupby('weather_group')[['casual', 'registered']].mean().reset_index()

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    sns.barplot(x='weather_group', y='casual', hue='weather_group', data=weather_analysis, palette='Blues_d', dodge=False, legend=False)
    plt.title('Rata-rata peminjaman pengguna biasa berdasarkan cuaca')
    plt.xlabel('Cuaca')
    plt.ylabel('Rata-rata peminjaman pengguna biasa')
    plt.legend([],[], frameon=False) 

    plt.subplot(1, 2, 2)
    sns.barplot(x='weather_group', y='registered', hue='weather_group', data=weather_analysis, palette='Greens_d', dodge=False, legend=False)
    plt.title('Rata-rata peminjaman pengguna terdaftar berdasarkan cuaca')
    plt.xlabel('Cuaca')
    plt.ylabel('Rata-rata peminjaman pengguna terdaftar')
    plt.legend([],[], frameon=False) 

    plt.tight_layout()
    st.pyplot(plt)

    st.caption("Pengguna casual dan pengguna registered cenderung melakukan peminjaman sepeda ketika cuaca cerah atau berkabut, hanya sebagian kecil pengguna yang melakukan peminjaman sepeda ketika salju ringan/hujan ringan, dan tidak pernah ada pengguna yang meminjam sepeda ketika badai salju/hujan lebat.")

elif visualization == "Pertanyaan 4":
    st.subheader("Seberapa besar pengaruh temperatur terhadap jumlah total transaksi bike sharing?")

    df['temp_bin'] = pd.cut(df['temp'], bins=[0, 0.3, 0.6, 1], labels=['Rendah', 'Sedang', 'Tinggi'])

    temp_analysis = df.groupby('temp_bin', observed=True)['cnt'].mean().reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='temp_bin', y='cnt', hue='temp_bin', data=temp_analysis, palette='coolwarm', dodge=False, legend=False)
    plt.title('Rata-rata total peminjaman berdasarkan kategori temperatur')
    plt.xlabel('Kategori Temperatur')
    plt.ylabel('Rata-rata total peminjaman')
    plt.legend([],[], frameon=False)
    st.pyplot(plt)

    st.caption("Transaksi peminjaman sepeda lebih banyak ketika temperatur tinggi, diikuti temperatur sedang, lalu paling sedikit saat temperatur rendah. Hal ini disebabkan karena pengguna menghindari cuaca salju ringan/hujan ringan dan badai salju/hujan lebat saat melakukan peminjaman sepeda ketika.")
