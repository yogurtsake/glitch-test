from flask import Flask
from livereload import Server, shell
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True
app.debug = True
bootstrap = Bootstrap(app)

from app import routes

server = Server(app.wsgi_app)
# server.watch
server.serve()
