import os

class Config:
    '''
    General configuration class
    '''
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_API_BASE_URL1 = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={}'
    NEWS_API_BASE_URL2 = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

    @staticmethod
    def init_app(app):
        pass
    

class ProdConfig(Config):

    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}

        