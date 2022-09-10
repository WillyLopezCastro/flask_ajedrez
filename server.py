from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html', num1=4, num2=4)


@app.route('/<int:num>')
def repeat(num):
    return render_template('index2.html', num1= num, num2=4)


@app.route('/<int:num1>/<int:num2>')
def repeat2(num1, num2):
    return render_template('index2.html', num1= num1, num2= num2)

if __name__=="__main__":
    app.run(debug=True)