from flask import Blueprint, render_template

index_app = Blueprint("index_app", __name__, url_prefix="/")


@index_app.route("/")
def index_view():
    return render_template("index.html")


@index_app.route("/about/")
def page_about():
    return render_template("about.html")


@index_app.route("/123/")
def page_about():
    return "123"
