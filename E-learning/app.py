from flask import render_template,request,Flask,redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy as _BaseSQLAlchemy
from sqlalchemy import desc

app=Flask(__name__)
#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://project_owner:n3TYGKsdQ1oA@ep-super-cloud-a1x157gx.ap-southeast-1.aws.neon.tech/project?sslmode=require'

# class for database preperation

class SQLAlchemy(_BaseSQLAlchemy):
    def apply_pool_defaults(self, app, options):
        super(SQLAlchemy, self).apply_pool_defaults(self, app, options)
        options["pool_pre_ping"] = True

# run database

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    title = db.Column(db.String(120), nullable=False)
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
        user = User(password=pwd, fullname=uname)
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
    return render_template("home.html",user=session['uname'])

questions = [
    {
        "question": "What is the primary purpose of programming languages?",
        "options": [
            "To enable computers to understand human emotions",
            "To enable humans to communicate instructions to computers",
            "To enhance graphics and sound in video games",
            "To design computer hardware"
        ],
        "answer": 1
    },
    {
        "question": "Which language was the earliest form of programming used to communicate directly with a computer's hardware?",
        "options": [
            "Assembly Language",
            "High-Level Language",
            "Machine Language",
            "Fourth-Generation Language"
        ],
        "answer": 2
    },
    {
        "question": "What is an example of a high-level programming language developed for scientific computing in 1957?",
        "options": [
            "COBOL",
            "FORTRAN",
            "Python",
            "JavaScript"
        ],
        "answer": 1
    },
    {
        "question": "Which type of programming language emerged in the 1970s and 1980s and is designed to be closer to natural human language?",
        "options": [
            "Machine Language",
            "Assembly Language",
            "Fourth-Generation Languages",
            "Low-Level Languages"
        ],
        "answer": 2
    },
    {
        "question": "Which programming paradigm is based on the concept of objects, which are instances of classes encapsulating data and behavior?",
        "options": [
            "Procedural Languages",
            "Functional Languages",
            "Object-Oriented Languages",
            "Scripting Languages"
        ],
        "answer": 2
    },
    {
        "question": "Which of the following is NOT a component of programming languages?",
        "options": [
            "Syntax",
            "Semantics",
            "Compilers",
            "Control Structures"
        ],
        "answer": 2
    },
    {
        "question": "Which language is known for its high-level, interpreted nature and is extensively used in data analysis and machine learning?",
        "options": [
            "C++",
            "JavaScript",
            "Python",
            "Ruby"
        ],
        "answer": 2
    },
    {
        "question": "Which language was designed by Apple for performance and safety, specifically for iOS and macOS app development?",
        "options": [
            "C#",
            "Swift",
            "Ruby",
            "Kotlin"
        ],
        "answer": 1
    },
    {
        "question": "What is a trend in programming languages that focuses on supporting multiple programming paradigms for greater flexibility?",
        "options": [
            "Development of Quantum Computing Languages",
            "Rise of Multi-Paradigm Languages",
            "Improved Performance and Efficiency",
            "Low-Code and No-Code Platforms"
        ],
        "answer": 1
    },
    {
        "question": "Which language is gaining traction due to its emphasis on memory safety and prevention of common programming errors that lead to security vulnerabilities?",
        "options": [
            "Rust",
            "C",
            "Prolog",
            "SQL"
        ],
        "answer": 0
    }
]
@app.route('/course',methods=['POST','GET'])
def course():
    if request.method=='POST':
       db.session.commit()
    return render_template("quizzes.html")

@app.route('/quiz')
def quiz():
    if request.method=='POST':
       db.session.commit()
    return render_template('quizzes.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for i, question in enumerate(questions):
        answer = int(request.form.get(f'question{i}'))
        if answer == question['answer']:
            score += 1
    return render_template('result.html', score=score, total=len(questions))
@app.route('/mycourse',methods=['POST','GET'])
def home():
    if request.method=='POST':
       db.session.commit()
    return render_template("home.html",user=session['uname'])
@app.route('/result')
def result():
    if request.method=='POST':
       db.session.commit()
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True,port=5001)