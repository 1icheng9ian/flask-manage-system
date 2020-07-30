# -*- encoding: utf-8 -*-
'''
@Time    :   2020/07/04
'''
import os, sys
from app import create_app
from flask_script import Manager, Server
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = create_app(os.getenv('config') or 'default')
manager = Manager(app)

manager.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True,
    host='127.0.0.1',
    port=8000))


if __name__ == "__main__":
    manager.run()