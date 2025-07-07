import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def cohort_analysis(df):
    df['OrderMonth'] = df['order_purchase_timestamp'].dt.to_period('M')
    df['CohortMonth'] = df.groupby('customer_id')['order_purchase_timestamp'].transform('min').dt.to_period('M')
    df['CohortIndex'] = (df['OrderMonth'].dt.year - df['CohortMonth'].dt.year) * 12 + \
                        (df['OrderMonth'].dt.month - df['CohortMonth'].dt.month)
    
    cohort_data = df.groupby(['CohortMonth', 'CohortIndex'])['customer_id'].nunique().unstack(1)
    cohort_sizes = cohort_data.iloc[:,0]
    retention = cohort_data.divide(cohort_sizes, axis=0)
    return retention

def plot_cohort_heatmap(retention):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(retention, annot=True, fmt='.0%', cmap='Blues', ax=ax)
    ax.set_title("Customer Retention by Cohort")
    ax.set_ylabel("Cohort Month")
    ax.set_xlabel("Months Since First Purchase")
    return fig
