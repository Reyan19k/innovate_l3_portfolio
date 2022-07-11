from flask import Flask, render_template, Blueprint, redirect, url_for

my_view = Blueprint('my_view', __name__)

@my_view.route('/')
def index():
    return render_template("index.html")

@my_view.route('/reyan')
def reyan():
    return render_template("reyan.html")

@my_view.route('/about')
def about():
    return render_template("about.html")

@my_view.route('/aboutme')
def about_redirect():
    return redirect(url_for("my_view.about"))


# @my_view.route('/pag2')
# @my_view.route('/pge2')
# @my_view.route('/pg2')
# @my_view.route('/pagetwo')
# def about_redirect():
#     return redirect(url_for("my_view.page2"))

# @my_view.route('/pag3')
# @my_view.route('/pge3')
# @my_view.route('/pg3')
# @my_view.route('/pagethree')
# def about_redirect():
#     return redirect(url_for("my_view.page3"))

# @my_view.route('/pag4')
# @my_view.route('/pge4')
# @my_view.route('/pg4')
# @my_view.route('/pagefour')
# def about_redirect():
#     return redirect(url_for("my_view.page4"))