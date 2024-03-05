from flask import Blueprint, render_template

sign_in = Blueprint("sign_in", __name__)


@sign_in.route("/")
def main():
    return render_template("sign_in.html")
