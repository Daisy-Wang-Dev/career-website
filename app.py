from flask import Flask, render_template, jsonify, request
from database import add_application_to_db, load_jobs_from_db, load_job_from_db

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

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)

  if not job:
    return "Not Found", 404
  return render_template("jobitem.html",job=job)

@app.route("/job/<id>/apply", methods=["POST"])
def apply(id):
  data = request.form

  add_application_to_db(id,data)
  
  return render_template("application_submitted.html", data=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)