"""Database models for the application."""

from flask_login import UserMixin

from . import db


class User(UserMixin, db.Model):
    """Represents a registered user."""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False, index=True)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:  # pragma: no cover - representation method
        return f"<User {self.email} ({self.role})>"
