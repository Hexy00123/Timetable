from flask import Flask, render_template
import json
import os

app = Flask(__name__)


@app.route('/')
def main_page():
    timetable = json.load(open("timetable.json", "r", encoding='utf-8'))

    return render_template('timetable.html', timetable=timetable)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
