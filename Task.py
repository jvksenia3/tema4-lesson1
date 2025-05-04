class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = "не выполнено"

    def mark_as_done(self):
        self.status = "выполнено"

    def __str__(self):
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {self.status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_as_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_done()


    def get_current_tasks(self):
        return [task for task in self.tasks if task.status == "не выполнено"]

# Пример использования
task_manager = TaskManager()
task_manager.add_task("Купить продукты", "2025-05-05")
task_manager.add_task("Помыть машину", "2025-05-06")

print("Текущие задачи:")
for task in task_manager.get_current_tasks():
    print(task)

task_manager.mark_task_as_done("Купить продукты")

print("\nТекущие задачи после выполнения одной:")
for task in task_manager.get_current_tasks():
    print(task)
