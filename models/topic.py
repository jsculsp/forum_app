from . import ModelMixin
from . import db


class Topic(db.Model, ModelMixin):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    node_id = db.Column(db.Integer, db.ForeignKey('nodes.id'))

    def __init__(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.node_id = form.get('node_id', '')

    def update(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.save()