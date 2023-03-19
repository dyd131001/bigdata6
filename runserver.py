from flask import Flask, make_response, jsonify
from service.user import User
from routes import main
from flask_login import LoginManager

app = Flask(__name__, static_url_path='/static')

# 임의의 값 실제 배포할때는 랜덤 값 주도록 바꾸기 (개발 때만 고정)
app.secret_key = "sdfieegrnqgono"

app.register_blueprint(main)

login_manager = LoginManager()
login_manager.init_app(app) # app 에 login_manager연결
login_manager.session_protection = "strong" # session 정보를 복잡하게 만듦


# 콜백, 세션에 저장된 사용자 ID에 사용자 개체를 다시 로드
@login_manager.user_loader
def load_user(id):
  return User.get(id)


@login_manager.unauthorized_handler
def unauthorized():
    # 로그인되어 있지 않은 사용자일 경우 401 에러 발생
    return make_response(jsonify(sussess=False), 401)
