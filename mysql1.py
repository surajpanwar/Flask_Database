from flask import Flask,request,jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host ="localhost", user ="suraj", passwd="ThisisMyPassword")
cursor=mydb.cursor()

cursor.execute("create database if not exists TaskDBAPI")
cursor.execute("create table if not exists TaskDBAPI.tasktable(name varchar(30), number int)")

@app.route('/insert',methods =['POST'])
def insert():
    if(request.method=='POST'):
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into TaskDBAPI.tasktable values (%s, %s)",(name,number))
        mydb.commit()
        return jsonify(str("Successfully Inserted"))

@app.route('/update',methods =['POST'])
def update():
    if request.method=='POST':
        name=request.json['get_name']  ## from api get_name will be passed and stored here
        cursor.execute("update TaskDBAPI.tasktable set number =number +500 where name =%s",(name,))
        mydb.commit()
        return jsonify(str("Updated successfully"))

@app.route('/delete',methods =['POST'])
def delete():
    if request.method =='POST':
        name_del = request.json['name_del']
        cursor.execute("delete from TaskDBAPI.tasktable where name =%s",(name_del,))
        mydb.commit()
        return jsonify(str("Deleted successfully"))

@app.route('/fetch',methods =['POST','GET'])
def fetch_data():
    if request.method == 'GET':
        cursor.execute("select * from TaskDBAPI.tasktable")
        l=[]
        for i in cursor.fetchall():
            l.append(i)
        return jsonify(str(l))


if __name__ =='__main__':
    app.run()
