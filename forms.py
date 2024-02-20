#Flask aapp to send message data
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        number = request.form['number']
        subject = request.form['subject']
        message = request.form['message']
    print(f"Name: {name}<br>Email: {email}<br>Number: {number}<br>Subject: {subject}<br>Message: {message}")

print('hit')

if __name__ == '__main__':
    app.run(debug=True)