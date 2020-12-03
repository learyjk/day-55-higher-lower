from flask import Flask
from random import randint
app = Flask(__name__)

num = randint(0, 9)
print(num)

@app.route('/')
def index():
    return '<h1>Guess a number between 0 and 9!</h1>' \
           '<img src="https://media4.giphy.com/media/xUn3CftPBajoflzROU/giphy.gif?cid=ecf05e479d7ql8gqis6emyrbpq4u8sxb39vgr111py9sbkug&rid=giphy.gif">'


@app.route('/<int:guess>')
def guessed(guess):
    if guess == num:
        return '<h1>correct!</h1>'
    elif guess > num:
        return '<h1>Too high!</h1>'
    else:
        return '<h1>Too low!</h1>'

if __name__ == "__main__":
    app.run(debug=True)