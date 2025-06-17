import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(filepath):
    df = pd.read_csv(filepath)
    analyzer = SentimentIntensityAnalyzer()
    df['sentiment'] = df['text'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
    return df[['text', 'sentiment']]

if _name_ == "_main_":
    sentiment_df = analyze_sentiment("data/tweets.csv")
    sentiment_df.to_csv("outputs/sentiments.csv", index=False)

