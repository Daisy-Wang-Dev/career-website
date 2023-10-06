from flask import Flask, render_template, jsonify

app = Flask(__name__)

Jobs = [
    {"id": 1, "title": "Data Analyst", "location": "New York, USA", "salary":"120,000"},
    {"id": 2, "title": "Software Engineer", "location": "San Francisco, USA", 
     "salary": "150,000"},
    {"id": 3, "title": "Marketing Manager", "location": "Los Angeles, USA", 
     "salary": "100,000"},
    {"id": 4, "title": "UX Designer", "location": "Chicago, USA", "salary": "110,000"}
]

# Can treat this like a api endpoint, it just renders html instead of JSON
@app.route("/")
def hello_world():
    return render_template("home.html", jobs = Jobs)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(Jobs)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)