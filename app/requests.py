import urllib.request, json
from datetime import datetime
from app import app
from .models import news
News = news.News

api_key = app.config['NEWS_API_KEY']
base_url1 = app.config['NEWS_API_BASE_URL1']
base_url2 = app.config['NEWS_API_BASE_URL2']

def get_news_by_country(country):
    '''
    Method to fetch news using the keyword - sources
    '''
    get_news_url = base_url1.format(country, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        response = json.loads(get_news_data)

        news_results = None

        if response['articles']:
            news_results_list = response['articles']
            news_results = process_results(news_results_list)

    return news_results


def process_results(news_list):
    '''
    Function that processes the news results and transforms them into a list of objects

    Args:
        news_list: a list of dictionaries containing news objests
    
    Returns:
        a news object
    '''

    news = []
    news_count = 1

    for item in news_list:
        id = news_count
        source = item.get('source')
        title = item.get('title')
        description = item.get('description')
        image_url = item.get('urlToImage')
        story_url = item.get('url')
        published_at = item.get('publishedAt')

        dateStr = published_at.split('T')
        date = dateStr[0]
        
        news_object = News(id, source, title, description, image_url, story_url, date)

        news.append(news_object)
        news_count +=1
    return news

def get_news_by_source(source):
    '''
    Method to fetch news using the keyword - sources
    '''
    get_news_url = base_url2.format(source, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        response = json.loads(get_news_data)

        news_results = None

        if response['articles']:
            news_results_list = response['articles']
            news_results = process(news_results_list)

    return news_results



def process(news_list):
    '''
    Function that processes the news results and transforms them into a list of objects

    Args:
        news_list: a list of dictionaries containing news objests
    
    Returns:
        a news object
    '''

    news = []
    news_count = 1

    for item in news_list:
        news_id = news_count
        source = item.get('source')
        title = item.get('title')
        description = item.get('description')
        image_url = item.get('urlToImage')
        story_url = item.get('url')
        published_at = item.get('publishedAt')

        dateStr = published_at.split('T')
        date = dateStr[0]
        
        news_object = News(news_id, source, title, description, image_url, story_url, date)

        news.append(news_object)
        news_count +=1
    return news

    


