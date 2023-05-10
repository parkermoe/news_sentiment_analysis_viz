import pandas as pd
from data_collection import collect_data
from preprocessing import clean_text
from sentiment_analysis import get_sentiment
from visualizations import generate_visualizations

def main():
    # Collect data
    df = collect_data()

    # Preprocess data
    df = clean_text(df)

    # Sentiment analysis
    df["sentiment"] = df["content"].apply(get_sentiment)

    # Generate visualizations
    generate_visualizations(df)

if __name__ == "__main__":
    main()
