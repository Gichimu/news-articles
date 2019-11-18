class News:
    '''
    class that defines the news object
    '''

    news_list = []

    def __init__(self, id, source, title, description, image_url, story_url, date_published):
        self.id = id
        self.source = source
        self.title = title
        self.description = description
        self.image_url = image_url
        self.story_url = story_url
        self.date_published = date_published

    def save_news(self):
        News.news_list.append(self)

    @classmethod
    def clear_news(cls):

        cls.news_list = []