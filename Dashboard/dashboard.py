import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

st.header("Dashboard Sederhana Anas")

#Import Dataset 1
order_payments_df = pd.read_csv("C:/Users/Anas G/Desktop/ANAS BELONGINGS/Dicoding_Analysis_Project/Data/order_payments_dataset.csv", delimiter=",")

with st.container():
    # Visualisasi 1
    st.title("Visualisasi Metode Pembayaran pada E-Commerce")
    plt.figure(figsize=(8, 6))
    order_payments_df['payment_type'].value_counts().plot(kind='bar', title='Metode Pembayaran pada E-Commerce', color='skyblue')
    plt.xlabel("Jenis Pembayaran")
    plt.ylabel("Jumlah Transaksi")
    st.pyplot(plt)
with st.expander("Penjelasan Visualisasi 1"):
    st.write(
        "Mayoritas transaksi pada e-cstommerce menggunakan metode credit_card atau kartu kredit. Disini muncul peluang untuk optimalisasi dimana e-commerce dapat fokus pada metode pembayaran kartu kredit dengan membuat promo menarik menggunakan metode pembayaran tersebut"
    )

# Import Dataset 2
order_items_df = pd.read_csv("C:/Users/Anas G/Desktop/ANAS BELONGINGS/Dicoding_Analysis_Project/Data/order_items_dataset.csv")
top_ten_seller = order_items_df['seller_id'].value_counts().head(10)

with st.container():
    # Visualisasi 2
    st.title("Top 10 Seller Berdasarkan Jumlah Order")
    plt.figure(figsize=(10, 6))
    top_ten_seller.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Top 10 Seller berdasarkan Jumlah Order', fontsize=16)
    plt.xlabel('Seller ID', fontsize=14)
    plt.ylabel('Jumlah Order', fontsize=14)
    for idx, value in enumerate(top_ten_seller.values):
        plt.text(idx, value + 2, str(value), ha='center', fontsize=10)
    plt.xticks(rotation=90)
    plt.tight_layout()
    st.pyplot(plt)
with st.expander("Penjelasan Visualisasi 2"):
    st.write(
        "Seller dengan ID 6560211a9b47992c3666c447a9e94c0 merupakan penjual dengan jumlah order tertinggi (2.033 order), diikuti oleh seller 4a3ca9b5744cef982374361493884 (1.987 order). Untuk seller dengan penjualan tertinggi bisa memberikan penawaran khusus seperti diskon untuk pelanggan setia, dan bagi seller dengan penjualan yang lebih rendah perlu dilakukan evaluasi strategi pemasaran ataupun jumlah promosi yang lebih banyak lagi"
    )