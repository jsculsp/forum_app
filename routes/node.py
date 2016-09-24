from models.node import Node
from models.topic import Topic
from routes import *

main = Blueprint('node', __name__)

pyid = id
Model = Node


@main.route('/')
def index():
    ms = Model.query.all()
    return render_template('node_index.html', node_list=ms)


@main.route('/<int:id>')
def show(id):
    m = Model.query.get(id)
    return render_template('node.html', node=m)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.save()
    return redirect(url_for('.index'))


@main.route('/edit/<int:id>')
def edit(id):
    m = Model.query.get(id)
    return render_template('node_edit.html', node=m)


@main.route('/delete/<int:id>')
def delete(id):
    m = Model.query.get(id)
    m.delete()
    return redirect(url_for('.index'))


@main.route('/update/<int:id>', methods=['POST'])
def update(id):
    form = request.form
    m = Model.query.get(id)
    m.update(form)
    return redirect(url_for('.index'))
