from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models import db
from models.todo import Todo
from models.node import Node
from models.topic import Topic

from routes.todo import main as routes_todo
from routes.node import main as routes_node
from routes.topic import main as routes_topic


app = Flask(__name__)
db_path = 'todo.sqlite'
manager = Manager(app)


def register_routes(app):
    app.register_blueprint(routes_todo, url_prefix='/todo')
    app.register_blueprint(routes_node, url_prefix='/node')
    app.register_blueprint(routes_topic, url_prefix='/topic')


def configure_app():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = 'hard_to_guess'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    db.init_app(app)
    register_routes(app)


def configured_app():
    configure_app()
    return app


@manager.command
def server():
    app = configured_app()
    config = dict(
        host='0.0.0.0',
        port = 80,
    )
    app.run(**config)


def configure_manager():
    """
    这个函数用来配置命令行选项
    """
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    configure_manager()
    configure_app()
    manager.run()