from app import app
from flask import request, render_template, redirect
from flask.helpers import url_for
import logging

@app.before_first_request
def initalize_logging():
    log_level = logging.INFO
    app.logger.setLevel(log_level)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        app.config["REGION"] = int(request.form["country_id"])
        app.logger.info("Someone sent a POST Call on the Home route")

    return render_template("home.html")

@app.route("/about-us", methods=["GET", "POST"])
def about_us():
    if request.method == "POST":
        redirect("/faq")

@app.route("/faq", methods=["GET", "POST"])
def faq():
    if request.method == "POST":
        app.logger.info("Someone sent a POST Call on the faq route")

    return render_template("faq.html")

@app.route("/catalog", methods=["GET", "POST"])
def catalog():
    if request.method == "POST":
        selected_product = request.form["product_id"]
        return redirect(url_for("product_details", country=app.config["REGION"], product_id=selected_product))

    elif request.method == "GET":
        return render_template("catalog.html")

@app.route("/catalog/<int:country>/<string:product_id>", methods=["GET", "POST"])
def product_details(country:int, product_id:str):
    if request.method == "POST":
        return render_template("order.html", country=country, product_id=product_id)

    elif request.method == "GET":
        options = [1,2,3]
        return render_template("product_details.html", country=country, product_id=product_id, options=options)
