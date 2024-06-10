from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
    'id1': 1,
    'title': 'Construction Manager',
    'location': 'Frederick, Colorado',
    'salary' : '$80,000'
    },
    {'id': 2,
     'title': 'Office Administrator',
     'location': 'Frederick Colorado',
     'salary' : '$45,000'
    },
    {'id': 3,
     'title': 'Engineer',
     'location': 'Remote'
    },
    {'id': 4,
     'title': 'Accountant',
     'location': 'Frederick, Colorado',
     'salary' : '$70,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name="Rockota")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
    

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)