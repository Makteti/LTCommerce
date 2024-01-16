# app/routes.py

from flask import Blueprint, render_template, request, redirect, url_for, session
from .models import Item  # Import your model(s) here

main_bp = Blueprint("main", __name__)
login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Here you can add your authentication logic
        # For simplicity, let's assume a hardcoded username and password
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "password":
            # Authentication successful, set the 'logged_in' session variable
            session['logged_in'] = True
            return redirect(url_for("main.index"))

    # If not authenticated or it's a GET request, render the login page
    return render_template("login.html")

@main_bp.route("/")
def index():
    # Check if the user is logged in before rendering the main page
    if not session.get('logged_in'):
        return redirect(url_for("login.login"))

    items = Item.select()
    return render_template("index.html", items=items)

@main_bp.route("/add", methods=["POST"])
def add_item():
    # Check if the user is logged in before processing the request
    if not session.get('logged_in'):
        return redirect(url_for("login.login"))

    # Add item logic here
    return redirect(url_for("main.index"))

@main_bp.route("/delete/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    # Check if the user is logged in before processing the request
    if not session.get('logged_in'):
        return redirect(url_for("login.login"))

    # Delete item logic here
    return redirect(url_for("main.index"))

@main_bp.route("/change_status/<int:item_id>", methods=["POST"])
def change_status(item_id):
    # Check if the user is logged in before processing the request
    if not session.get('logged_in'):
        return redirect(url_for("login.login"))

    # Change status logic here
    return redirect(url_for("main.index"))

@main_bp.route("/logout", methods=["POST"])
def logout():
    # Clear the 'logged_in' session variable on logout
    session.pop('logged_in', None)
    return redirect(url_for("login.login"))
