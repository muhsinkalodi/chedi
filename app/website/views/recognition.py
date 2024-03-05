from flask import Blueprint, render_template

recognition = Blueprint('recognition', __name__)

@recognition.route('/')
def main():
    return render_template('recognition.html', recognition_active='active')
