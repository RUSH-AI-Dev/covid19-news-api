import json
import credentials
import pandas as pd
from pymongo import MongoClient

#pip install pymongo
#pip install pymongo[srv]

def insert_voice(filename='voice.xlsx'):
#connection to MongoDB
    voice = pd.read_excel(filename)
    con = MongoClient(credentials.host)
    db = con.get_database(credentials.cluster)
    obj = db.VoiceNews
    print("Connected successfully!!!")
    obj.insert(json.loads(voice.to_json()))
    con.close()
    print("Insert_voice to MongoDB Successful")

def insert_dailynews(filename='dailynews.xlsx'):
#connection to MongoDB
    dailynews = pd.read_excel(filename)
    con = MongoClient(credentials.host)
    db = con.get_database(credentials.cluster)
    obj = db.DailynewsNews
    print("Connected successfully!!!")
    obj.insert(json.loads(dailynews.to_json()))
    con.close()
    print("Insert_dailynews to MongoDB Successful")

def insert_nation(filename='nation.xlsx'):
#connection to MongoDB
    nation = pd.read_excel(filename)
    con = MongoClient(credentials.host)
    db = con.get_database(credentials.cluster)
    obj = db.NationNews
    print("Connected successfully!!!")
    obj.insert(json.loads(nation.to_json()))
    con.close()
    print("Insert_nation to MongoDB Successful")

def insert_sanook(filename='sanook.xlsx'):
#connection to MongoDB
    sanook = pd.read_excel(filename)
    con = MongoClient(credentials.host)
    db = con.get_database(credentials.cluster)
    obj = db.SanookNews
    print("Connected successfully!!!")
    obj.insert(json.loads(sanook.to_json()))
    con.close()
    print("Insert_sanook to MongoDB Successful")

def insert_thairath(filename='thairath.xlsx'):
#connection to MongoDB
    thairath = pd.read_excel(filename)
    con = MongoClient(credentials.host)
    db = con.get_database(credentials.cluster)
    obj = db.ThairathNews
    print("Connected successfully!!!")
    obj.insert(json.loads(thairath.to_json()))
    con.close()
    print("Insert_thairath to MongoDB Successful")
