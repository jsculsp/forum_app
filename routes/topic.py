from models.topic import Topic
from routes import *

main = Blueprint('topic', __name__)

pyid = id
Model = Topic


@main.route('/')
def index():
    ms = Model.query.all()
    return render_template('topic_index.html', topic_list=ms)


@main.route('/<int:id>')
def show(id):
    m = Model.query.get(id)
    if m is None:
        abort(404)
    return render_template('topic.html', topic=m)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.save()
    return redirect(url_for('node.show', id=m.node_id))


@main.route('/edit/<int:id>')
def edit(id):
    m = Model.query.get(id)
    return render_template('topic_edit.html', topic=m)


@main.route('/delete/<int:id>')
def delete(id):
    m = Model.query.get(id)
    m.delete()
    return redirect(url_for('node.show', id=m.node_id))


@main.route('/update/<int:id>', methods=['POST'])
def update(id):
    form = request.form
    m = Model.query.get(id)
    m.update(form)
    return redirect(url_for('node.show', id=m.node_id))
