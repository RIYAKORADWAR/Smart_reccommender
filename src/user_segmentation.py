import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def segment_users(df):
    user_df = df.groupby('user_id').agg({
        'event_type': lambda x: x.value_counts().to_dict()
    }).reset_index()

    # Expand dictionary column
    user_df = user_df.join(pd.json_normalize(user_df['event_type']))
    user_df = user_df.fillna(0).drop('event_type', axis=1)

    scaler = StandardScaler()
    features = scaler.fit_transform(user_df.drop('user_id', axis=1))

    kmeans = KMeans(n_clusters=4, random_state=42)
    user_df['segment'] = kmeans.fit_predict(features)
    return user_df

if _name_ == "_main_":
    ecommerce_df = pd.read_csv("outputs/cleaned_data.csv")
    segmented = segment_users(ecommerce_df)
    segmented.to_csv("outputs/user_segments.csv", index=False)
