import config
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
from newsapi import NewsApiClient
from tqdm import tqdm

def fetch_articles(newsapi, source_list, query_term):
    articles = []
    for source in source_list:
        source_articles = newsapi.get_everything(q=query_term, sources=source, language='en', sort_by='relevancy')
        articles.extend(source_articles['articles'])
    return articles

def get_article_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')

        content = '\n'.join([paragraph.get_text() for paragraph in paragraphs])
        return content
    except Exception as e:
        print(f"Error fetching content from {url}: {e}")
        return None

def fetch_and_save_data(newsapi, query_terms, left_wing_sources, right_wing_sources):
    for query_term in query_terms:
        print(f"Fetching articles for {query_term}")
        left_wing_articles = fetch_articles(newsapi, left_wing_sources, query_term)
        right_wing_articles = fetch_articles(newsapi, right_wing_sources, query_term)


        articles_data = {
            f'{query_term}_left_wing_articles': left_wing_articles,
            f'{query_term}_right_wing_articles': right_wing_articles
        }

        with open(f'articles_data_{query_term}.json', 'w') as file:
            json.dump(articles_data, file, ensure_ascii=False, indent=4)

        with open(f'articles_data_{query_term}.json', 'r') as file:
            articles_data = json.load(file)

        total_articles = sum([len(articles_data[f'{query_term}_{wing}_articles']) for wing in ['left', 'right'] if f'{query_term}_{wing}_articles' in articles_data])
        print(f"Fetching full content for {total_articles} articles")
        for group in tqdm(articles_data):
            if f'{query_term}_left_wing_articles' in group or f'{query_term}_right_wing_articles' in group:
                for i, article in enumerate(articles_data[group]):
                    url = article['url']
                    content = get_article_content(url)
                    if content:
                        articles_data[group][i]['content'] = content

        with open(f'articles_data_full_content_{query_term}.json', 'w') as file:
            json.dump(articles_data, file, ensure_ascii=False, indent=4)

        flattened_data = []

        for wing, group in tqdm(zip(['left', 'right'], [f'{query_term}_left_wing_articles', f'{query_term}_right_wing_articles'])):
            articles_group = articles_data[group]
            for article in articles_group:
                flat_article = {
                    'query': query_term,
                    'wing': wing,
                    'source_name': article['source']['name'],
                    'author': article['author'],
                    'title': article['title'],
                    'description': article['description'],
                    'published_at': article['publishedAt'],
                    'content': article['content'] if 'content' in article else None
                }
                flattened_data.append(flat_article)

        df = pd.DataFrame(flattened_data)
        df.to_csv(f'articles_data_{query_term}.csv', index=False)
        return df
     
    
 def get_news(NEWSAPI, query_term):
    newsapi = NewsApiClient(api_key=NEWSAPI)
    
    # Add the lists of your chosen left wing and right wing sources here
    left_wing_sources = ['cnn', 'msnbc']
    right_wing_sources = ['fox-news', 'breitbart-news']

    # Call the fetch_and_save_data function with the provided query term
    return fetch_and_save_data(newsapi, [query_term], left_wing_sources, right_wing_sources)
