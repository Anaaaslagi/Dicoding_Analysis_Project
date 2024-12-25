import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Import Dataset 1 
order_payments_df = pd.read_csv("Data/order_payments_dataset.csv", delimiter=",")

# Import Dataset 2 
order_items_df = pd.read_csv("Data/order_items_dataset.csv")

# Menghitung Top 10 Seller berdasarkan jumlah order
top_ten_seller = order_items_df['seller_id'].value_counts().head(10)

# Judul Dashboard
st.title('Dashboard Transaksi')
st.write('Pilih metode pembayaran untuk melihat data transaksi yang sesuai:')

# Sidebar untuk filter metode pembayaran
selected_methods = st.multiselect(
    'Metode Pembayaran:', 
    options=order_payments_df['payment_type'].unique(), 
    default=order_payments_df['payment_type'].unique()
)

# Filter data berdasarkan metode pembayaran yang dipilih
filtered_data = order_payments_df[order_payments_df['payment_type'].isin(selected_methods)]

# Menampilkan data yang difilter dalam bentuk tabel
st.subheader('Data Transaksi Berdasarkan Metode Pembayaran')
st.dataframe(filtered_data)

# Visualisasi Top 10 Seller berdasarkan jumlah order
st.subheader("Top 10 Seller Berdasarkan Jumlah Order")
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
