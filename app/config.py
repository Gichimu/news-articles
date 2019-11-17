class Config:
    '''
    General configuration class
    '''

    NEWS_API_BASE_URL1 = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={}'
    NEWS_API_BASE_URL2 = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    

class ProdConfig(Config):

    pass

class DevConfig(Config):
    DEBUG = True

        