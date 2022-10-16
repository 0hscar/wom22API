import os, requests, psycopg2

conn = psycopg2.connect(database="postgres", user = "ohscar", password ="!Kakan123", host="wom22.postgres.database.azure.com", port = "5432")

print("Opened database successfully")


def testRun():
    cur = conn.cursor()

    cur.execute("INSERT INTO services (service) \
        VALUES ('Testing')");

    conn.commit()


def fetchAll():
    cur =  conn.cursor()
    
    cur.execute("SELECT * FROM services")
    rows = cur.fetchall()
    for row in rows:
        print("service = "), row[1]
    
    
def deleteTest():
    cur = conn.cursor()
    
    cur.execute("DELETE from SERVICES where service=testing")
    conn.commit()
    
fetchAll()
    

# api_url = "http://host=wom22.postgres.database.azure.com port=5432 dbname={postgres} user=ohscar password={!Kakan123} sslmode=require"

# response = requests.get(api_url)
# response.json()
# {"service": "Taktvätt"}

