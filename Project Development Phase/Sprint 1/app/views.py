from app import app
from flask import render_template

@app.route('/')
def home():
    return  render_template('home.html')

@app.route('/headlines')
def headlines():
    return  render_template('headlines.html')

@app.route('/articles')
def articles():
    return  render_template('articles.html')

@app.route('/sources')
def sources():
    return  render_template('sources.html')

@app.route('/category/business')
def business():
    return  render_template('business.html')

@app.route('/category/tech')
def tech():
    return  render_template('tech.html')

@app.route('/category/entertainment')
def entertainment():
    return  render_template('entertainment.html')

@app.route('/category/science')
def science():
    return  render_template('science.html')

@app.route('/category/sports')
def sports():
    return  render_template('sport.html')

@app.route('/category/health')
def health():
    return  render_template('health.html')