from flask import render_template,request,Flask,redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy as _BaseSQLAlchemy

app=Flask(__name__)
#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://project_owner:n3TYGKsdQ1oA@ep-super-cloud-a1x157gx.ap-southeast-1.aws.neon.tech/project?sslmode=require'

# class for database preperation

class SQLAlchemy(_BaseSQLAlchemy):
    def apply_pool_defaults(self, app, options):
        super(SQLAlchemy, self).apply_pool_defaults(self, app, options)
        options["pool_pre_ping"] = True


db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    title = db.Column(db.String(120))
    grades = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()

app.secret_key="superhighsecretlock"

@app.route('/',methods=['POST','GET'])
def login():
    msg=''
    if request.method=='POST':
        uname = request.form["uname"]
        pwd = request.form["pswd"]
        auth = User.query.filter_by(fullname=uname,password=pwd).all()
        if auth:
            session['uname']=uname
            session['pwd']=pwd
            return redirect(url_for('home'))
        else:
            msg="Invalid Username/Password"
    return render_template("login.html",message=msg)

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=="POST":
        uname = request.form["uname"]
        pwd = request.form["pswd"]
        user = User(password=pwd, fullname=uname,grades=0)
        db.session.add(user)
        db.session.commit()
        if user:
            session['uname']=uname
            session['pwd']=pwd
            return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/home',methods=['POST','GET'])
def home():
    if request.method=='POST':
       db.session.commit()
    return render_template('home.html',user=session['uname'])


@app.route('/course',methods=['POST','GET'])
def course():
    if request.method=='POST':
       db.session.commit()
    return render_template("courses.html")

@app.route('/course_details',methods=['POST','GET'])
def course_details_1():
    if request.method=='POST':
       db.session.commit()
    return render_template("course_details1.html")

@app.route('/course_details2',methods=['POST','GET'])
def course_details_2():
    if request.method=='POST':
       db.session.commit()
    return render_template("course_details2.html")

@app.route('/course_details3',methods=['POST','GET'])   
def course_details_3():
    if request.method=='POST':
       db.session.commit()
    return render_template("course_details3.html")

@app.route('/course_details4',methods=['POST','GET'])
def course_details_4():
    if request.method=='POST':
       db.session.commit()
    return render_template('services.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method=='POST':
       db.session.commit()
    return render_template('quizzes.html')

@app.route('/quiz1', methods=['GET', 'POST'])
def quiz1():
    if request.method=='POST':
       db.session.commit()
    return render_template('quiz1.html')

@app.route('/quiz2', methods=['GET', 'POST'])
def quiz2():
    if request.method=='POST':
       db.session.commit()
    return render_template('quiz2.html')

@app.route('/quiz3', methods=['GET', 'POST'])
def quiz3():
    if request.method=='POST':
       db.session.commit()
    return render_template('quiz3.html')




@app.route('/submit', methods=['POST','GET'])
def submit():
    score=request.json['score']
    print(score)
    return redirect(url_for('result', score=score))



@app.route('/mycourse',methods=['POST','GET'])
def mycourses():
    if request.method=='POST':
       db.session.commit()
    return render_template("mycourses.html",user=session['uname'])


@app.route('/result/<int:score>',methods=['GET'])
def result(score):
    print("hello")
    return render_template('result.html',score=score)


@app.route('/service',methods=['POST','GET'])
def service():
    if request.method=='POST':
       db.session.commit()
    return render_template("service.html")
@app.route('/about',methods=['POST','GET'])
def about():
    if request.method=='POST':
       db.session.commit()
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True,port=5001)