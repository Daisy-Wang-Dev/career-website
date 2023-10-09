from sqlalchemy import create_engine, text
import sqlalchemy
import os

db_string = os.environ['DB_CONNECTION_STRING']

engine=create_engine(db_string, 
 connect_args= {
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",            
        }
    }          
)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = []

    for row in result.all():
      jobs.append(row._asdict())
  
  return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM jobs WHERE id = :id"), {'id': id}
    )

    rows = result.all()

    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()
  
def add_application_to_db(job_id, application):
  with engine.connect() as conn:
    query = text("INSERT INTO application(job_id, full_name, email, linkedin_url) VALUES (:job_id, :full_name, :email, :linkedin_url)")

    result = conn.execute(query, 
      {"job_id":job_id,
      "full_name":application["full_name"],
      "email":application["email"],
      "linkedin_url":application["linkedin"]
      }
    )
                
  return