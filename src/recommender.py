import pandas as pd
from sklearn.neighbors import NearestNeighbors

def build_recommender(df, sentiment_df):
    ratings = df[df['event_type'] == 'purchase']
    user_product = ratings.pivot_table(index='user_id', columns='product_id', aggfunc='size', fill_value=0)

    model = NearestNeighbors(metric='cosine')
    model.fit(user_product)

    # Dummy logic for demonstration
    recommendations = []
    for user_id in user_product.index:
        _, indices = model.kneighbors([user_product.loc[user_id]], n_neighbors=3)
        recommended_products = user_product.columns[indices[0]].tolist()
        recommendations.append((user_id, recommended_products))

    rec_df = pd.DataFrame(recommendations, columns=['user_id', 'recommended_products'])
    return rec_df

if _name_ == "_main_":
    ecommerce_df = pd.read_csv("outputs/cleaned_data.csv")
    sentiment_df = pd.read_csv("outputs/sentiments.csv")
    rec_df = build_recommender(ecommerce_df, sentiment_df)
    rec_df.to_csv("outputs/recommendations.csv", index=False)

