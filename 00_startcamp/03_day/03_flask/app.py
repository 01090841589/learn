from flask import Flask, render_template, request
import random, requests
app = Flask(__name__)

@app.route('/catch')
def catct:
    retuen render_template('catch_html')

@app.route('/result')
def result():
    #1. form 태그로 날린 데이터를 받는다
    word = request.args.get('word')
    fonts = request.get('http://artii.herokuapp.com/fonts_list').text
    fonts = fonts.split('\n')
    font = random.choice(fonts)
    request.get(f'http://artii.herokuapp.com/fonts_list/make?text={word}&font={font}').text
    return render_template('result.html', result = result )