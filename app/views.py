from flask import render_template
import random
from flask_paginate import Pagination, get_page_parameter
from app import app
from .requests import get_news_by_country, get_news_by_source

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    country = 'us'


    news = get_news_by_country(country)
    
    # pagination = Pagination(page=page, total=news.count())
    title = "Welcome to your most comprehensive news hub"
    return render_template('index.html', news = news)


@app.route('/article/<int:id>')
def article(id):
    '''
    View article page function that returns the individual article
    '''
    country = 'us'


    news = get_news_by_country(country)

    for item in news:
        if item.id == id:
            article = item
    
    return render_template('article.html', article = article)


@app.route('/sources/<source>')
def articles(source):
    '''
    View articles page function that returns the list of articles on a particular source
    '''

    news = get_news_by_source(source)
    pages = len(news)/5

    return render_template('news.html', news = news)


@app.route('/sources/<source>/<int:id>')
def news(source, id):
    '''
    View articles page function that returns the list of articles on a particular source
    '''

    news = get_news_by_source(source)

    for x in news:
        if x.id == id:
            art = x

    return render_template('article2.html', art = art)
