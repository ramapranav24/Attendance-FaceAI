from flask import Flask, render_template, redirect, url_for
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mark', methods=['POST'])
def mark_attendance():
    try:
        subprocess.run(['python', 'mark_attendance.py'])
        return redirect(url_for('index'))
    except Exception as e:
        return f"<h2>Error occurred:</h2><pre>{str(e)}</pre>"

@app.route('/view')
def view_attendance():
    if os.path.exists('attendance.csv'):
        with open('attendance.csv', 'r') as f:
            lines = f.read().splitlines()
            return "<h2>Attendance Log</h2>" + "<br>".join(lines) + '<br><br><a href="/">Back</a>'
    return "No attendance file found."

if __name__ == '__main__':
    app.run(debug=True)
