from flask import request
from flask import Flask
from flask import render_template
import pyodbc
import os
from azure.storage.blob import BlobClient, BlobServiceClient
app = Flask(__name__,template_folder='template')
basedir = os.path.abspath(os.path.dirname(__file__))
@app.route("/", methods=['GET','POST'])

def hello_world():
    row=["Na","Na"]
    if request.method=='POST':
        pno=request.form['phno']
        print(pno)
        server = 'assignmentservershruthaja.database.windows.net'
        database = 'assignment1'
        username = 'shruthaja'
        password = 'mattu4-12'
        driver = '{ODBC Driver 17 for SQL Server}'
        conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        cursor = conn.cursor()
        query = "SELECT descript,pic FROM dbo.q0c where teln=?"
        cursor.execute(query,pno)
        row = cursor.fetchone()
        print(row[0],row[1])
    return render_template("index.html",desc=row[0],imglink=row[1])
@app.route("/roomrange", methods=['GET','POST'])
def room():
    row=["no information or picture available","no information or picture available","no information or picture available"]
    if request.method=='POST':
        start=request.form['start']
        end=request.form['end']
        server = 'assignmentservershruthaja.database.windows.net'
        database = 'assignment1'
        username = 'shruthaja'
        password = 'mattu4-12'
        driver = '{ODBC Driver 17 for SQL Server}'
        conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        cursor = conn.cursor()
        query = "SELECT name,descript,pic FROM dbo.q0c where room between ?  and ?"
        cursor.execute(query,start,end)
        row = cursor.fetchall()
        data=[]
        for i in row:
            data.append(i)
    return render_template("index.html",data=data)

@app.route("/newdesc.html", methods=['GET','POST'])
def change():
    row = ["Na", "Na"]
    if request.method == 'POST':
        name = request.form['name']
        desc=request.form['description']
        server = 'assignmentservershruthaja.database.windows.net'
        database = 'assignment1'
        username = 'shruthaja'
        password = 'mattu4-12'
        driver = '{ODBC Driver 17 for SQL Server}'
        conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        cursor = conn.cursor()
        query = "update dbo.q0c set descript=? where name=?"
        cursor.execute(query,desc, name)
        cursor.commit()
        query = "SELECT name,descript from dbo.q0c where name=?"
        cursor.execute(query, name)
        row = cursor.fetchone()
    return render_template("newdesc.html",row=row)

if __name__ == "__main__":
    app.run(debug=True)