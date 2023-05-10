import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from wordcloud import WordCloud
from collections import defaultdict
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
# import counter

def generate_visualizations(df):
    # filtering the dataframe to only include CNN, Fox News, and MSNBC
    df = df[df['source_name'].isin(['CNN', 'Fox News', 'MSNBC'])]

    # Get the sentiment counts per author
    sentiment_counts = df.groupby('source_name')['sentiment'].value_counts().unstack().fillna(0)

    # Sort the authors by the total number of articles
    sorted_authors = sentiment_counts.sum(axis=1).sort_values(ascending=False).index

    # Select the top 10 authors
    top_sentiment_counts = sentiment_counts.loc[sorted_authors[:10]]

    # Plot the stacked bar chart
    ax = top_sentiment_counts.plot(kind='bar', stacked=True, figsize=(10, 6))
    ax.set_title('Sentiment Counts per News Source')
    ax.set_ylabel('Number of Articles')

    # Display the legend
    ax.legend(title='Sentiment', bbox_to_anchor=(1, 1))

    plt.show()


    news_sources = ['CNN', 'MSNBC', 'Fox News']

    # Concatenate all article contents for each news source
    source_contents = defaultdict(str)
    for _, row in df.iterrows():
        source = row['source_name']
        content = row['content']
        if isinstance(content, str):
            source_contents[source] += content

    # Define a color function for the word cloud
    def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        source = word_sources[word]
        if source == "CNN":
            return "red"
        elif source == "MSNBC":
            return "blue"
        elif source == "Fox News":
            return "green"

    def generate_word_frequencies(text, stopwords):
        words = word_tokenize(text)
        words = [word for word in words if word.lower() not in stopwords and word.isalpha()]
        tagged_words = pos_tag(words)
        nouns = [word for word, pos in tagged_words if pos in ["NN", "NNS", "NNP", "NNPS"]]
        word_frequencies = defaultdict(int)
        for noun in nouns:
            word_frequencies[noun] += 1
        return word_frequencies


    # Create a stricter set of stopwords
    strict_stopwords = set(stopwords.words('english'))
    strict_stopwords.update(["said", "first", "last", "will", 'Monday','month', 'months', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'week', 'weeks', 'year', 'years', 'day', 'days', 'weekend', 'weekends', 'today', 'tomorrow', 'yesterday', 'morning', 'afternoon', 'evening', 'night', 'evenings', 'nights', 'weekdays', 'weeknights'
    , 'Solutions', 'minutes', 'broadcast', 'people',])

    news_sources = ['CNN', 'MSNBC', 'Fox News']
    # Calculate the word frequencies for each source after removing stop words
    source_word_frequencies = {}
    for source in news_sources:
        content = source_contents[source]
        word_frequencies = generate_word_frequencies(content, strict_stopwords)
        source_word_frequencies[source] = word_frequencies

    # Select the top N words from each source
    N = 50
    top_words = {}
    for source in news_sources:
        word_frequencies = source_word_frequencies[source]
        top_words[source] = dict(Counter(word_frequencies).most_common(N))

    # Combine the top words for all sources
    combined_top_words = defaultdict(int)
    word_sources = {}
    for source in news_sources:
        for word, freq in top_words[source].items():
            combined_top_words[word] += freq
            word_sources[word] = source

    # Generate the word cloud with different colors for each source and without stop words
    wordcloud = WordCloud(stopwords=strict_stopwords, background_color="white", width=800, height=400)
    wordcloud.generate_from_frequencies(frequencies=combined_top_words)
    wordcloud.recolor(color_func=color_func)
    plt.figure(figsize=(16, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Combined Word Cloud")
    plt.show()
