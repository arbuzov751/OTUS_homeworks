"""
Домашнее задание №4
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""

from flask import Flask, render_template
# from views.index import index_app


app = Flask(__name__)
# app.register_blueprint(index_app)


@app.route("/")
def index_view():
    return render_template("index.html")


@app.route("/about/")
def page_about():
    return render_template("about.html")


@app.route("/123/")
def page_test():
    return "123"


if __name__ == "__main__":
    app.run(debug=True)
