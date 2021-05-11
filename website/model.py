from flask import Flask, Blueprint, request, redirect, url_for, render_template
from pymongo import MongoClient
import urllib

client = MongoClient("mongodb+srv://admin-triyam:"+urllib.parse.quote_plus("Chinum1@*")+"@cluster0.gx0f2.mongodb.net/cb?retryWrites=true&w=majority")
db = client['cb']['amazoncb']
collection = db
print(db)

# searchreasult = request.args.get('q')
# result = db.find_one({"name":  request.args.get('q')})

        