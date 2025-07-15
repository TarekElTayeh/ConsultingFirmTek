from flask_login import login_required, current_user
from flask import abort

@client.route('/client_dashboard')
@login_required
def client_dashboard():
    if current_user.role != 'client':
        abort(403)
    return render_template('client_dashboard.html')