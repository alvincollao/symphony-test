class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str):
        if not task.strip():
            raise ValueError("Task cannot be empty")
        self.tasks.append(task)
        return True

    def list_tasks(self):
        return self.tasks

    def remove_task(self, task: str):
        if task in self.tasks:
            self.tasks.remove(task)
            return True
        return False


if __name__ == "__main__":
    app = TodoApp()
    app.add_task("Learn unit testing")
    app.add_task("Push project to GitHub")
    print("Tasks:", app.list_tasks())