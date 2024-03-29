import functools

from flask import Blueprint, current_app
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from .db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")

def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view

@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = (
            get_db().execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
        )


@bp.route("/register", methods=("GET", "POST"))
def register():
    """Register a new user.

    Validates that the username is not already taken. Hashes the
    password for security.
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                # The username was already taken, which caused the
                # commit to fail. Show a validation error.
                error = f"User {username} is already registered."
            else:
                # Success, go to the login page.
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None
        user = db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password."

        if error is None:
            # store the user id in a new session
            session.clear()
            session["user_id"] = user["id"]
            create_databases
            

            # if the user is maintenance, redirect to maintenance page
            if username == "m" and password == "1234":
                return redirect(url_for("maintenance.home"))
            
                        # if the user is maintenance, redirect to maintenance page
            if username == "maintenance" and password == "password":
                return redirect(url_for("maintenance.home"))
            
             # if the user is engineer, redirect to engineer page
            if username == "e" and password == "1234":
                return redirect(url_for("engineer.home"))
            
             # if the user is engineer, redirect to engineer page
            if username == "engineer" and password == "password":
                return redirect(url_for("engineer.home"))

            # if the user is operator, redirect to operator page
            if username == "o" and password == "1234":
               return redirect(url_for("operator.home"))
            
                        # if the user is operator, redirect to operator page
            if username == "operator" and password == "password":
               return redirect(url_for("operator.home"))

            # otherwise, redirect to the index
            return redirect(url_for("index"))

        flash(error)

    return render_template("auth/login.html")



@bp.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("index"))

def create_databases():

            db = get_db()

             # List of your SQL databases to force initalize upon login
            sql_files = ['past_alarms.sql', 'current_alarms.sql', 'operator_tables.sql']

            for sql_file in sql_files:
                with current_app.open_resource(sql_file) as f:
                    db.executescript(f.read().decode("utf8"))