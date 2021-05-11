from flask import Blueprint, render_template, redirect, url_for, request
from .model import db
import requests
from bs4 import BeautifulSoup

views = Blueprint('views', __name__)

@views.route("/", methods=['GET', 'POST'])
def home():
    print(db)
    try:
        searchimage = ''
        searchprice = ''
        searchquery = request.args.get('q')
        result = db.find_one({"name":  searchquery})
        searchprice = result['price']
        searchimage = result['image']
        print(searchquery)
        print(result)
        print(searchprice)

        # flipkart

        # try:
        #     from googlesearch import search
        # except ImportError:
        #     print("No module named 'google' found")

        # query = searchquery + " flipkart"

        # for j in search(query, tld="com", num=1, stop=1, pause=0):
        #     link = j
        #     print(link)
        # html_text = requests.get(link).text
        # soup = BeautifulSoup(html_text, 'lxml')
        # flipkart_price = soup.find("div", class_="_30jeq3 _16Jk6d").text
        # flipkart_details = soup.find("div", class_="_2418kt").text
        # flipkart_name = soup.find("span", class_="B_NuCI").text
        
        if searchquery != None:
            return redirect(url_for("views.search", result=result))
    except TypeError as ex:
        print("Item not available")
    
    return render_template('home.html', template_folder="templates")

@views.route("/search/<result>", methods=['GET', 'POST'])
def search(result):
    return render_template("product.html",result=result)
