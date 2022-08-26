'''from flask import Flask,request,jsonify

import pymongo

app=Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://suraj:suraj123@cluster0.f8ooe.mongodb.net/?retryWrites=true&w=majority")
database=client['taskdbapi']
collection=database['apitaskcollection']

@app.route('/insert/mongo',methods =['POST'])
def insert():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name,number})
        return  jsonify(str("successfully instered mongodata"))

if __name__ =='__main':
    app.run()'''

from flask import Flask, request, jsonify
import pymongo
client = pymongo.MongoClient("mongodb+srv://suraj:suraj123@cluster0.f8ooe.mongodb.net/?retryWrites=true&w=majority")

app = Flask(__name__)


database = client['taskdbapi']
collection = database['apitaskcollection']


@app.route("/mongoinsert", methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name: number})
        return jsonify(str("successfully inserted "))


if __name__ == '__main__':
    app.run()