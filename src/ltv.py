import pandas as pd

def calculate_ltv(df):
    payments = df[['order_id', 'customer_id', 'payment_value']]
    ltv = payments.groupby('customer_id')['payment_value'].sum().reset_index()
    ltv.columns = ['customer_id', 'ltv']
    # Gabungkan dengan cluster jika ada
    if 'cluster' in df.columns:
        ltv = ltv.merge(df[['customer_id', 'cluster']].drop_duplicates(), on='customer_id', how='left')
    return ltv
