from flask import render_template

# 404 page not find
def page_not_found(e):
    return render_template('errors/404.html'), 404

# 401 Authorization access
def handle_unauthorized(e):
    return render_template('errors/401.html'), 401

# 403 forbidden access
def handle_forbidden(e):
    return render_template('blog_admin/403.html', msg=e.description), 403
