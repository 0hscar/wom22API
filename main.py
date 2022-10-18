from ast import Str
import os, requests, psycopg2
from pickletools import unicodestring1
import unicodedata
from dotenv import load_dotenv

load_dotenv()




connectURL = os.environ.get('CONNECTURL')
conn = psycopg2.connect(
    user = os.environ.get('DATABASE_USERNAME'),
    password = os.environ.get('DATABASE_PASSWORD'),
    host = os.environ.get('DATABASE_HOST'),
    port = os.environ.get('DATABASE_PORT'),
    database = os.environ.get('DATABASE_NAME')
)

print("Opened database successfully")


def testRun():
    cur = conn.cursor()

    cur.execute("INSERT INTO services (service) \
        VALUES ('Testing')");

    conn.commit()


def fetchServices():
    cur =  conn.cursor()
    
    cur.execute("SELECT * FROM services")
    rows = cur.fetchall()
    for row in rows:
        print("service = "), row[1]
    
    
def deleteTest():
    cur = conn.cursor()
    
    cur.execute("DELETE from SERVICES where service=testing")
    conn.commit()
    
# fetchServices()
    

# api_url = "http://host=wom22.postgres.database.azure.com port=5432 dbname={postgres} user=ohscar password={!Kakan123} sslmode=require"

# response = requests.get(api_url)
# response.json()
# {"service": "Taktvätt"}

