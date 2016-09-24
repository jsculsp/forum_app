from models.todo import Todo
from routes import *

main = Blueprint('todo', __name__)

pyid = id
Model = Todo


@main.route('/')
def index():
    ms = Model.query.all()
    return render_template('todo_index.html', todo_list=ms)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    t = Model(form)
    t.save()
    return redirect(url_for('.index'))


@main.route('/edit/<int:id>')
def edit(id):
    t = Model.query.get(id)
    return render_template('todo_edit.html', todo=t)


@main.route('/delete/<int:id>')
def delete(id):
    t = Model.query.get(id)
    t.delete()
    return redirect(url_for('.index'))


@main.route('/update/<int:id>', methods=['POST'])
def update(id):
    form = request.form
    t = Model.query.get(id)
    t.update(form)
    return redirect(url_for('.index'))