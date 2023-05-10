import pandas as pd
import nltk
from get_news import get_news
from clean_news import clean_text
from sentiment_analysis import get_sentiment
from visualizations import generate_visualizations

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

NEWSAPI = 'YOUR_NEWSAPI_KEY_HERE'
query_term = 'climate change'

def main():
    # Collect data
    df = get_news(NEWSAPI, query_term)

    # Preprocess data
    df = clean_text(df)

    # Sentiment analysis
    df["sentiment"] = df["content"].apply(get_sentiment)

    # Generate visualizations
    generate_visualizations(df)

if __name__ == "__main__":
    main()

