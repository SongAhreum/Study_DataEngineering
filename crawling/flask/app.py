from flask import Flask, render_template
from scoreRouter import score
# score=Blueprint('score',__name__)

app = Flask(__name__)
app.register_blueprint(score, url_prefix='/score')

# route정의 
# welcome page
@app.route('/') #이 경로로 접근할 때 실행될 함수가 아래에 정의
def index(): return render_template('index.html', title='홈페이지')

if __name__ == '__main__': app.run(port=5001, debug=True)

# __name__은 현재 모듈이름을 나타내는 특수한 변수 (실행스크립으이름)
# 스크립트가 직접 실행될 때는 __name__이 '__main__'이 됨
# 모듈로 임포트되면 모듈의 이름이 됨