import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def generate_rfm(df, n_clusters=6):
    # Hitung RFM
    reference_date = pd.to_datetime(df['order_purchase_timestamp']).max()
    rfm = df.groupby('customer_id').agg({
        'order_purchase_timestamp': lambda x: (reference_date - pd.to_datetime(x.max())).days,
        'order_id': 'nunique',
        'payment_value': 'sum'
    }).reset_index()
    rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']

    # Clustering
    X = rfm[['recency', 'frequency', 'monetary']]
    X_scaled = StandardScaler().fit_transform(X)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    rfm['cluster'] = kmeans.fit_predict(X_scaled)
    return rfm
