"""Authentication routes."""

import logging

from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .forms import LoginForm, SignupForm
from .models import User


logger = logging.getLogger(__name__)


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    """Authenticate an existing user."""

    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
        except SQLAlchemyError as exc:  # pragma: no cover - database error
            logger.error("Database error during login for %s: %s", form.email.data, exc)
            flash("An internal error occurred. Please try again later.", "error")
        else:
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("client.dashboard"))
            flash("Invalid email or password.", "error")
    return render_template("login.html", form=form)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    """Register a new user and log them in."""

    form = SignupForm()
    if form.validate_on_submit():
        try:
            if User.query.filter_by(email=form.email.data).first():
                flash("Email address already registered.", "error")
            else:
                user = User(
                    email=form.email.data,
                    password=generate_password_hash(form.password.data),
                    role="client",
                )
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for("client.dashboard"))
        except SQLAlchemyError as exc:  # pragma: no cover - database error
            db.session.rollback()
            logger.error("Failed to create user %s: %s", form.email.data, exc)
            flash("Could not create account. Please try again later.", "error")
    return render_template("signup.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    """Log out the current user."""

    logout_user()
    return redirect(url_for("auth.login"))

