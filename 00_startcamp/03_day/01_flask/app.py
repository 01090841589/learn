from flask import Flask
import datetime
import random
app = Flask(__name__)

@app.route('/')
def hello():
    return 'HIHIHIHIHIHIHIHIHIHI'

@app.route('/ssafy')
def ssafy():
    return 'this is SSAFY'

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    endgame = datetime.datetime(2019, 11, 29)
    td = endgame - today
    return f'SSAFY 1학기 종료까지 {td.days} 일 남았습니다.'

@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag!</h1>'

    
@app.route('/html_line')
def html_line():
    return '''
    <h1> 여러줄로 작성하자!</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>    
    '''
@app.route('/greeting/<string:name>')
def greeting(name):
    return f'반갑습니다! {name}님!'
    
@app.route('/cube/<int:number>')
def mul(number):
    return f'{number}의 세제곱은 {number**3}입니다!'

#점심 메뉴 리스트(5개)에서 2개를 뽑아 출력하기
@app.route('/menu/<int:person>')
def menu(person):
    menu = '쇠고기볶음', '갈치카레구이', '빨간우동', '아몬드치킨 샌드위치', '프라이두부샐러드'
    lunch = random.sample(menu, person)
    return f'{str(lunch)}먹으세요!'
    