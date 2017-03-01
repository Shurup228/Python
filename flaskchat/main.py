from flask import Flask, render_template, redirect
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_object('config')
#x

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


@app.route('/')
def root():
    return redirect('/index')


@app.route('/index')
def index():
    user_ = {'nickname': 'andriy'}
    lst = ["mem", "xyu", "bib"]
    return render_template("index.html", title="root", user=user_, memeslist=lst)

if __name__ == '__main__':
    app.run(debug=True)
