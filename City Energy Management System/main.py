import os
from flask import Flask,render_template,request,session,flash,redirect,url_for
from dbconfig import db, init_app
from models import User,EnergyDevice,EnergyType,Area
from usersControl import users_bp
from comControl import energy_bp


app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(energy_bp, url_prefix='/energy')

init_app(app)

# 创建表,如果已经存在表，怎跳过
with app.app_context():
    db.create_all()

# 这个部分主要是完成登录注册

@app.route('/', methods=['GET','POST'])
def login():
    error_message = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            session['username'] = user.username
            flash('登录成功！', 'success')
            return redirect(url_for('home'))
        else:
            error_message = '用户名或密码错误'
    return render_template('login.html', error_message=error_message)

@app.route('/register', methods=['GET','post'])
def register():
    error_message = None
    exist_user_error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        gender = request.form.get('gender')
        age = request.form.get('age')

        if username and password:
            existing_user = User.query.filter_by(username = username).first()
            if existing_user:
                exist_user_error = '用户名已存在，请选择其他用户注册'
            else:
                new_user = User(username = username,password = password,gender=gender,age = age)
                db.session.add(new_user)
                db.session.commit()
                flash('注册成功！请登录。','success')
                return redirect(url_for('login'))
        else:
            error_message = '请填写用户名和密码'
    return render_template('register.html',error_message=error_message, exist_user_error=exist_user_error)


@app.route('/home')
def home():
    if 'username' not in session:
        flash('请先登录', 'error')
        return redirect(url_for('login'))

    username = session['username']
    # 从数据库中获取用户数据，并传递给前端渲染
    userdatas = User.query.all();
    # 获取类型数据，传给前端渲染
    energytypes = EnergyType.query.all();
    # 获取区域数据，传给前端渲染
    areas = Area.query.all();
    # 获取类型数据，传给前端渲染
    devices = EnergyDevice.query.all();

    return render_template('home.html', userdatas=userdatas,username=username, energytypes=energytypes, areas=areas,devices=devices)

@app.route('/logout')
def logout():
    session.clear()
    flash('您已退出登录', 'info')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)