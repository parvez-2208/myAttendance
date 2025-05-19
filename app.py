from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
users = {'admin': 'password123'}  # Example user

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            return redirect(url_for('attendance'))
        return "Invalid credentials"
    return render_template('login.html')

@app.route('/attendance')
def attendance():
    return render_template('attendance.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


