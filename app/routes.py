from flask import render_template
from . import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/adoption')
def adoption():
    return render_template('adoption.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')