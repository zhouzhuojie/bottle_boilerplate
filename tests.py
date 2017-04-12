import mock
from main import get_one
from models import Todo

class TestTodos:

    @mock.patch('main.Todo.get_one')
    def test_todo_get_one(self, mock_get_one):
        mock_todo = Todo()
        mock_todo.id = 1001
        mock_todo.name = 'mock name'
        mock_get_one.return_value = mock_todo

        t = get_one(1001)
        assert t.get('id') == 1001
