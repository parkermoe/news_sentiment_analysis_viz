# News Sentiment Analysis + Visualization

This project is a sentiment analysis tool built in Python to analyze and visualize the sentiment of news articles related to climate change. The project uses the NewsAPI to fetch news articles from various sources, NLTK for preprocessing and sentiment analysis, and Matplotlib, Plotly, and Wordcloud for visualization.

## Overview

The project has four main steps:

1. Fetching news articles related to climate change.
2. Cleaning and preprocessing the articles.
3. Performing sentiment analysis on the articles.
4. Visualizing the results.

## Usage

To use this project, follow these steps:

1. Clone the repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Replace `'YOUR_NEWSAPI_KEY_HERE'` in `main.py` with your NewsAPI key.
4. Replace `query_term` in main.py with your query of interest
5. Run `main.py` to execute the script and generate the visualizations.

## Code Structure

Here's a brief description of the different components of the code:

- `main.py`: This is the main script that you run to execute the project. It calls the other scripts and functions.

- `get_news.py`: This script contains the `get_news` function, which fetches news articles related to climate change from NewsAPI.

- `clean_news.py`: This script contains the `clean_text` function, which cleans and preprocesses the articles. It removes stopwords, punctuation, and other unnecessary elements.

- `sentiment_analysis.py`: This script contains the `get_sentiment` function, which performs sentiment analysis on the articles using `"nlptown/bert-base-multilingual-uncased-sentiment"`.

- `visualizations.py`: This script contains the `generate_visualizations` function, which generates various visualizations based on the results of the sentiment analysis. It generates a bar chart showing the sentiment counts for different news sources, a treemap showing the sentiment counts for the top authors from each source, and a word cloud showing the most common words used in the articles.

## Output

The script will output several visualizations:

1. A bar chart showing the sentiment counts for different news sources.
2. A treemap showing the sentiment counts for the top authors from each source.
3. A word cloud showing the most common words used in the articles.

## Dependencies

This project uses the following libraries:

- pandas
- NLTK
- matplotlib
- plotly
- wordcloud
- requests
- numpy
- torch
- transformers
- beautifulsoup4
- newsapi-python

These can be installed via pip using the command `pip install -r requirements.txt`.

## Note

Please note that the NewsAPI key is required to fetch the articles. You can get a key by signing up on the [NewsAPI website](https://newsapi.org/).

This project is meant to be a starting point for your sentiment analysis projects. Feel free to modify and adapt it to suit your needs.
