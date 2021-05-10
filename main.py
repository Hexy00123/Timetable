from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    timetable = json.load(open("timetable.json", "r", encoding='utf-8'))

    if request.method == 'POST':
        week = request.form.get('week')
        if not week:
            week = 'Чётная'
        return render_template('timetable.html', timetable=timetable, week = week)

    return render_template('timetable.html', timetable=timetable, week = 'Чётная')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
