# Customer Segmentation & Retention Dashboard

Proyek ini menganalisis data pelanggan dari Olist untuk memahami perilaku konsumen melalui **RFM Segmentation**, **Cohort Retention Analysis**, dan **Lifetime Value (LTV)**.

Dibuat menggunakan **Streamlit** untuk visualisasi interaktif dan digunakan sebagai bagian dari portofolio Data Science.

---

## Tujuan

- Mengelompokkan pelanggan berdasarkan **recency, frequency, dan monetary value (RFM)**
- Melacak **retensi pelanggan** berdasarkan cohort bulanan
- Mengestimasi **Customer Lifetime Value** berdasarkan cluster RFM
- Menyajikan insight melalui **dashboard interaktif**

---


## Fitur Dashboard

- **Dataset Overview**  
  Tampilkan sampel data dan insight awal.

- **Cohort Analysis**  
  Heatmap yang menunjukkan retensi pelanggan dari cohort bulanan.

- **RFM Segmentation**  
  Segmentasi pelanggan berdasarkan perilaku pembelian.

- **Lifetime Value**  
  Visualisasi nilai pelanggan per segmen RFM.

---

## Cara Menjalankan Dashboard

1. Install dependency:

```bash
pip install -r requirements.txt
```

2. Jalankan Streamlit

`cd dashboard`
`streamlit run app.py`

## Dataset
Dataset yang digunakan adalah dataset publik dari Olist:

Download dari: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
