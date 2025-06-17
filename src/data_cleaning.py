import pandas as pd

def clean_ecommerce_data(filepath):
    df = pd.read_csv(filepath)
    df = df.dropna(subset=['event_type', 'product_id', 'user_id'])
    df['event_time'] = pd.to_datetime(df['event_time'])
    return df

if _name_ == "_main_":
    df = clean_ecommerce_data("data/ecommerce_data.csv")
    df.to_csv("outputs/cleaned_data.csv", index=False)

