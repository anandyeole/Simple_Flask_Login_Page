# importing packages
from project import userDetails, db
from flask import Blueprint, render_template, url_for, redirect, request, flash
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from flask_login import login_user, login_required, logout_user, current_user

# blueprint of the auth which needs to be imported to __init__.py
auth = Blueprint("auth", __name__)


# login_Form elements
class loginForm(FlaskForm):
    email = StringField(
        "Email Addresss",
        validators=[DataRequired(), Email(message="Enter Valid Email")],
    )
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


# signup_Form elements
class signupForm(FlaskForm):
    email = StringField(
        "Email Address", validators=[DataRequired(), Email(message="Enter Valid Email")]
    )
    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

    # check email at the time of form filling --> needs to implemented properly later(#todo)
    def check_email(self, field):
        if userDetails.query.filter_by(email=field.data).first():
            raise ValidationError("Your Email already Registered")


# Route for login page
@auth.route("/login", methods=["GET", "POST"])
def login():
    login_Form = loginForm()

    # proceed only if all values of form are filled and validated
    if login_Form.validate_on_submit():

        # if this returns a user, then the email already exists in database
        user = userDetails.query.filter_by(email=login_Form.email.data).first()

        # if user not present or wrong password flash message and let user try again
        if user == None or not user.check_password(login_Form.password.data):
            flash("Email Not registered or wrong password")

        else:
            # double check if password is correct or not
            if user.check_password(login_Form.password.data) and user is not None:
                login_user(user)
                flash("Login Successful")
                # If a user was trying to visit a page that requires a login
                # flask saves that URL as 'next'.
                next = request.args.get("next")

                # So let's now check if that next exists, otherwise we'll go to
                # the profile page.
                if next == None or not next[0] == "/":
                    next = url_for("profile")

                return redirect(next)
            # return render_template('profile.html', name=current_user.name)

    # render login page for form filling
    return render_template("login.html", form=login_Form)


# Route for signup page
@auth.route("/signup", methods=["GET", "POST"])
def signup():

    signup_Form = signupForm()

    # proceed only if all values of form are filled and validated
    if signup_Form.validate_on_submit():
        user = userDetails(
            email=signup_Form.email.data,
            name=signup_Form.name.data,
            password=signup_Form.password.data,
        )

        # if email already present in the database then go to signup page
        if userDetails.query.filter_by(email=user.email).first() != None:
            flash("Email already registered")
            return render_template("signup.html", form=signup_Form)

        else:
            # Add user to the database
            db.session.add(user)
            db.session.commit()
            flash("Signup Successfull")

        # After successfull signup go to login page
        return redirect(url_for("auth.login"))

    # render signup page for form filling
    return render_template("signup.html", form=signup_Form)


# Route to Logout user
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("User Successfully Logged out")
    return redirect(url_for("home"))
