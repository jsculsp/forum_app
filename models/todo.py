from . import ModelMixin
from . import db
from . import created_time


class Todo(db.Model, ModelMixin):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String())
    created_time = db.Column(db.Integer)
    updated_time = db.Column(db.Integer)

    def __init__(self, form):
        self.task = form.get('task', '')
        self.created_time = created_time()

    def update(self, form):
        self.task = form.get('task', '')
        self.updated_time = created_time()
        self.save()