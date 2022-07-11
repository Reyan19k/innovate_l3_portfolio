from flask import Flask, Blueprint, render_template, redirect, url_for

my_view = Blueprint('my_view', __name__)

@my_view.route('/')
def index():
    return render_template ("index.html")

@my_view.route('/page1')
def page1():
    return render_template("page1.html")

@my_view.route('/pag1')
@my_view.route('/pg1')
@my_view.route('/pge1')
def page1_redirect():
    return redirect(url_for("my_view.page1"))

@my_view.route('/page2')
def page2():
    return render_template("page2.html")

@my_view.route('/pag2')
@my_view.route('/pg2')
@my_view.route('/pge2')
def page2_redirect():
    return redirect(url_for("my_view.page2"))


@my_view.route('/page3')
def page3():
    return render_template("page3.html")

@my_view.route('/pag3')
@my_view.route('/pg3')
@my_view.route('/pge3')
def page3_redirect():
    return redirect(url_for("my_view.page3"))

@my_view.route('/page4')
def page4():
    return render_template("page4.html")

@my_view.route('/pag4')
@my_view.route('/pg4')
@my_view.route('/pge4')
def page4_redirect():
    return redirect(url_for("my_view.page4"))

@my_view.route('/admin')
def admin():
    return render_template("admin.html")

@my_view.route('/amin')
@my_view.route('/admn')
@my_view.route('/adin')
def admin_redirect():
    return redirect(url_for("my_view.admin"))

@my_view.route('/javascript')
@my_view.route('/js')
@my_view.route('/home')
def index_redirect():
    return redirect(url_for("my_view.index"))