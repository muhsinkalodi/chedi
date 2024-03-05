from flask import Blueprint, render_template

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/")
def main():
    return render_template("dashboard.html", dashboard_active="active")
