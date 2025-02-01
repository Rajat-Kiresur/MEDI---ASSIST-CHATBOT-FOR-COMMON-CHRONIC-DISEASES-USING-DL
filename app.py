from flask import Flask, render_template, request, jsonify
import chatt  # Import your chat_not_used.py script
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/team')
def team():
    team_members = [
        {"name": "Santrapti Nayak", "usn": "2KE20CS083", "email": "santrapti@gmail.com"},
        {"name": "Rohini G Navade", "usn": "2KE20CS072", "email": "rohini@gmail.com"},
        {"name": "Saakshi Shet", "usn": "2KE20CS073", "email": "saakshi@gmail.com"},
        {"name": "Rajat Kiresur", "usn": "2KE20CS066", "email": "rajat@gmail.com"}
    ]
    return render_template('team.html', team_members=team_members)


@app.route('/symptoms')
def symptoms():
    with open('pattern.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        symptoms_list = [row[0] for row in reader]
    return render_template('symptoms.html', symptoms=symptoms_list)


@app.route('/faq')
def faq():
    with open('patterns.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        symptoms_list = [row[0] for row in reader]
    return render_template('faq.html', symptoms=symptoms_list)


@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        symptoms = request.json['symptoms']
        message = ', '.join(symptoms)  # Join symptoms into a single string
        response = chatt.get_response(chatt.predict_class(message), chatt.intents)
        return response
    except Exception as e:
        print("Be Clear with your symptom:", e)
        return "Be Clear with your symptom"


if __name__ == '__main__':
    app.run(debug=True)
