from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_object('config')


class LoginForm(FlaskForm):
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


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run(debug=True)
