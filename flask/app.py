#app.py
from flask import Flask, render_template, redirect, request, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import String, JSON
import psycopg2 #pip install psycopg2 
import psycopg2.extras
from psycopg2.extras import RealDictCursor

import json
app = Flask(__name__)
     
app.secret_key = "caircocoders-ednalan"
     
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "postgres"


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
     
engine = create_engine("mysql://"+DB_USER+":"+DB_PASS+"@"+DB_HOST+"/"+DB_NAME, echo=True)
    
@app.route("/get_hour",methods=["POST","GET"])
def get_child_categories():
    cur = conn.cursor(cursor_factory=RealDictCursor)    
    if request.method == 'POST':
        day = request.form['day']
        hour = request.form['hour']
        week = request.form['week']
        cur.execute("SELECT * FROM four_week_condensed WHERE day = %s AND hour = %s AND week = %s", [day,hour,week])
        hour = cur.fetchone()
    return render_template('response.html', hour=hour)
    
    
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
@app.route('/', methods=['GET', 'POST'])
def index():
    with engine.connect() as connection:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        json_payload=None
        if request.method == 'POST':
            print("posting")
            day = request.form['day']
            hour = request.form['hour']
            week = request.form['week']
            print(day,hour,week)
            result = connection.execute(text("SELECT * FROM four_week_condensed WHERE day = :d AND hour = :h AND week = :w"),[{"d":day,"h":hour,"w":week}])
            #cur.execute()
            #json_payload = cur.fetchone()
            json_payload = dict(result.one())
            print(json_payload)
            
        else:
            cur.execute("SELECT * FROM four_week_condensed ORDER BY id")
            json_payload = cur.fetchone()
        result = cur.execute("SELECT week FROM four_week_condensed GROUP BY week")
        weeks = cur.fetchall()
        
        result = cur.execute("SELECT day FROM four_week_condensed GROUP BY day")
        days = cur.fetchall()
        
        result = cur.execute("SELECT hour FROM four_week_condensed GROUP BY hour")
        hours = cur.fetchall()
        
        if json_payload == None:
            json_payload={}
        print(json_payload)
        return render_template('index.html', curval=json_payload, weeks = weeks, days = days, hours = hours)
        
    #curval = loaddata(app_root + "/edwin.json")
    #return render_template('index.html', curval=json.dumps(employee))
if __name__ == "__main__":
    app.run(debug=True)