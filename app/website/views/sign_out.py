from flask import Blueprint, render_template

sign_out = Blueprint("sign_out", __name__)


@sign_out.route("/")
def main():
    return render_template("sign_out.html")
