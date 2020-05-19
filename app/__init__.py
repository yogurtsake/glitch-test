from flask import Flask
from livereload import Server, shell

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True
app.debug = True

from app import routes

server = Server(app.wsgi_app)
# server.watch
server.serve()
