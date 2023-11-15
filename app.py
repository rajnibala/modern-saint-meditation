from flask import Flask, render_template, jsonify
app = Flask(__name__)
PROGRAMS = [
  {
    'Program': 1,
    'title': 'Personal Meditation Classes',
    'Location': 'Online',
    'Fees': 'Rs. 2999/-'
  },
  {
    'id': 2,
    'title': 'Group Meditation Classes',
    'Location': 'Online',
    'Fees': 'Rs. 999/-'
  },
  {
    'id': 3,
    'title': 'Personal Counselling',
    'Location': 'Online',
    'Fees': 'Rs. 899/-'
  },
  {
    'id': 4,
    'title': 'Relationship Counselling',
    'Location': 'Online',
    'Fees': 'Rs. 899/-'
  },
  {
    'id': 5,
    'title': 'Parental Counselling',
    'Location': 'Online',
    'Fees': 'Rs. 899/-'
  },
  {
    'id': 6,
    'title': 'Student Counselling',
    'Location': 'Online',
    'Fees': 'Rs. 899/-'
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
