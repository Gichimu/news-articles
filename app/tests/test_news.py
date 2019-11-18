import unittest
from app.models import News

class Test_news(unittest.TestCase):
    '''
    Class the functionality in the news model
    '''

    def setUp(self):
        '''
        Method that runs on every test
        '''

        self.news_item = News(3, 'Test title', 'Test description', 'Test story url', 'Test image url', '2019-4-3')


    def test_instance(self):
        '''
        Test to check that each instantiation is done correctly in the model
        '''

        self.assertEqual(isinstance(self.news_item, News))