from src.data_cleaning import clean_ecommerce_data
from src.sentiment_analysis import analyze_sentiment
from src.user_segmentation import segment_users
from src.recommender import build_recommender

if _name_ == "_main_":
    print("[1] Cleaning e-commerce data...")
    ecommerce_df = clean_ecommerce_data("data/ecommerce_data.csv")
    ecommerce_df.to_csv("outputs/cleaned_data.csv", index=False)

    print("[2] Performing sentiment analysis...")
    sentiment_df = analyze_sentiment("data/tweets.csv")
    sentiment_df.to_csv("outputs/sentiments.csv", index=False)

    print("[3] Segmenting users...")
    segments = segment_users(ecommerce_df)
    segments.to_csv("outputs/user_segments.csv", index=False)

    print("[4] Generating recommendations...")
    rec_df = build_recommender(ecommerce_df, sentiment_df)
    rec_df.to_csv("outputs/recommendations.csv", index=False)

    print("✅ All done. Check the outputs folder.")
