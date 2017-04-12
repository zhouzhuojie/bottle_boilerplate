import bottle

from models import Todo, Comment

app = bottle.Bottle()

@app.get('/todos/:id')
def get_one(id):
    todo = Todo.get_one(id)
    return todo.as_dict()

@app.get('/todos')
def get_all():
    todos = Todo.get_all()
    return { 'todos': [t.as_dict() for t in todos] }

@app.put('/todos/:id')
def put_one(id):
    todo = Todo.put_one(id, bottle.request.json)
    return todo.as_dict()

@app.post('/todos')
def post_one():
    todo = Todo.post_one(bottle.request.json)
    return todo.as_dict()

@app.post('/todos/:id/comments')
def post_one_comment(id):
    c = Comment()
    c.todo_id = id
    c.message = bottle.request.json.get('message')
    c.save()
    return c.as_dict()

@app.get('/todos/:id/comments')
def get_comments(id):
    todo = Todo.get_one(id)
    return { 'comments': [c.as_dict() for c in todo.comments] }

if __name__ == '__main__':
    app.run(server='tornado', port=8080, reloader=True)
