from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def main_page():
    timetable = json.load(open("timetable.json", "r", encoding='utf-8'))

    return render_template('timetable.html', timetable=timetable)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
