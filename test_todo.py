import pytest
from todo import TodoApp

def test_add_task():
    app = TodoApp()
    assert app.add_task("Write tests")
    assert "Write tests" in app.list_tasks()

def test_add_empty_task():
    app = TodoApp()
    with pytest.raises(ValueError):
        app.add_task("")

def test_remove_task():
    app = TodoApp()
    app.add_task("Clean code")
    assert app.remove_task("Clean code")
    assert "Clean code" not in app.list_tasks()

def test_remove_nonexistent_task():
    app = TodoApp()
    assert not app.remove_task("Doesn't exist")