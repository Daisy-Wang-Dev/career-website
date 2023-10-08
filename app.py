from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)


# Can treat this like a api endpoint, it just renders html instead of JSON
@app.route("/")
def hello_world():
    Jobs = load_jobs_from_db()
    return render_template("home.html", jobs = Jobs)

@app.route("/api/jobs")
def list_jobs():
    Jobs = load_jobs_from_db()
    return jsonify(Jobs)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)