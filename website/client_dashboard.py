"""Client dashboard views."""

import logging

from flask import Blueprint, abort, render_template
from flask_login import current_user, login_required


client = Blueprint("client", __name__)
logger = logging.getLogger(__name__)


def _is_client(user) -> bool:
    """Return True if the given user has the client role."""

    return getattr(user, "role", None) == "client"


@client.route("/client_dashboard")
@login_required
def dashboard():
    """Render the dashboard for authenticated client users."""

    if not _is_client(current_user):
        logger.warning("Unauthorized dashboard access attempt by user %s", getattr(current_user, "id", "anonymous"))
        abort(403)
    return render_template("client_dashboard.html")

