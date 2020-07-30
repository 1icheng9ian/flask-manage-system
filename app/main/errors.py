from flask import render_template

# 404 page not find
def page_not_found(e):
    return render_template('errors/404.html'), 404
