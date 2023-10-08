from flask import Flask, render_template, jsonify
app = Flask(__name__)
PROGRAMS = [
  {
    'Program': 1,
    'title': 'Personal online meditation classes alternate days',
    'Location': 'Remote',
    'Fees': 'Rs. 2999/-'
  },
  {
    'id': 2,
    'title': 'Online group classes of (3-5) alt days',
    'Location': 'Remote',
    'Fees': 'Rs. 999/-'
  },
  {
    'id': 3,
    'title': 'Personal Counselling',
    'Location': 'Remote',
    'Fees': 'Rs. 599/-'
  },
  {
    'id': 4,
    'title': 'Relationships Counselling',
    'Location': 'Remote',
    'Fees': 'Rs. 599/-'
  },
  {
    'id': 5,
    'title': 'Parental Counselling',
    'Location': 'Remote',
    'Fees': 'Rs. 599/-'
  },
  {
    'id': 6,
    'title': 'Child Counselling',
    'Location': 'Remote',
    'Fees': 'Rs. 599/-'
  }
]

@app.route("/")
def hello_MSM():
    return render_template('Home.html',Programs=PROGRAMS, company_name='MSM')

@app.route("/api/Programs")
def list_Programs():
    return jsonify(PROGRAMS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
