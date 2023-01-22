#app.py
from flask import Flask, render_template, redirect, request, flash, jsonify
import psycopg2 #pip install psycopg2 
import psycopg2.extras
     
app = Flask(__name__)
     
app.secret_key = "caircocoders-ednalan"
     
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "postgres"
         
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
     
@app.route('/')
def index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM four_week ORDER BY id")
    employee = cur.fetchall()
    return render_template('index.html', employee=employee)
  
@app.route("/ajax_add",methods=["POST","GET"])
def ajax_add():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        txtname = request.form['txtname']
        txtposition = request.form['txtposition']
        txtoffice = request.form['txtoffice']
        print(txtname)
        if txtname == '':
            msg = 'Please Input name' 
        elif txtposition == '':
           msg = 'Please Input Position' 
        elif txtoffice == '':
           msg = 'Please Input Office' 
        else:        
            cur.execute("INSERT INTO employee (name,position,office) VALUES (%s,%s,%s)",[txtname,txtposition,txtoffice])
            conn.commit()       
            cur.close()
            msg = 'New record created successfully'  
    return jsonify(msg)
  
@app.route("/ajax_update",methods=["POST","GET"])
def ajax_update():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        string = request.form['string']
        txtname = request.form['txtname']
        txtposition = request.form['txtposition']
        txtoffice = request.form['txtoffice']
        print(string)
        cur.execute("UPDATE employee SET name = %s, position = %s, office = %s WHERE id = %s ", [txtname, txtposition, txtoffice, string])
        conn.commit()       
        cur.close()
        msg = 'Record successfully Updated'  
    return jsonify(msg)    
  
@app.route("/ajax_delete",methods=["POST","GET"])
def ajax_delete():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        getid = request.form['string']
        print(getid)
        cur.execute('DELETE FROM employee WHERE id = {0}'.format(getid))
        conn.commit()       
        cur.close()
        msg = 'Record deleted successfully'  
    return jsonify(msg) 
 
if __name__ == "__main__":
    app.run(debug=True)