# importing packages
from flask import Flask, render_template
from flask_login import login_required, current_user
from project import db, app


# Home page Route
@app.route('/')
def home():
    return render_template('home.html')


# Profile page route
@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    # defining function
    return render_template("404.html")


# Run the app
if __name__ == "__main__":
    app.run()
