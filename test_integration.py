from todo import TodoApp

def test_full_workflow():
    app = TodoApp()
    # Add tasks
    app.add_task("Task A")
    app.add_task("Task B")
    # Verify list
    tasks = app.list_tasks()
    assert "Task A" in tasks and "Task B" in tasks
    # Remove one
    app.remove_task("Task A")
    assert "Task A" not in app.list_tasks()