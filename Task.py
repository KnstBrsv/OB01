from datetime import datetime, timedelta

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d')  # Ожидается формат даты: ГГГГ-ММ-ДД
        self.completed = False  # По умолчанию задача не выполнена
        print(f"Задача <{self.description}> создана!")

    def complete_task(self):
        self.completed = True # Помечает задачу как выполненную
        print(f"Задача <{self.description}> выполнена!")

    def is_overdue(self):
        return datetime.now() >= self.due_date + timedelta(days=1) and not self.completed

    def __str__(self): # Возвращает информацию о задаче (переопределенный метод)
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Дедлайн: {self.due_date.date()}, Статус: {status}"

# Функция для вывода всех текущих (не выполненных) задач
def display_current_tasks(tasks):
    current_tasks = [task for task in tasks if not task.completed]
    if not current_tasks:
        print("Все задачи выполнены!")
    else:
        print("Текущие задачи:")
        for task in current_tasks:
            print(task)
# Функция для вывода всех просроченных задач
def display_overdue_tasks(tasks):
    overdue_tasks = [task for task in tasks if task.is_overdue()]
    if not overdue_tasks:
        print("Нет просроченных задач!")
    else:
        print("Просроченные задачи:")
        for task in overdue_tasks:
            print(task)

# Пример использования
task1 = Task("Сделать домашнее задание", "2024-10-20")
task2 = Task("Позвонить врачу", "2024-10-17")
task3 = Task("Сдать отчет", "2024-10-18")

# Завершим одну из задач
task2.complete_task()

# Список задач
tasks = [task1, task2, task3]

# Вывод всех текущих (не выполненных) задач
display_current_tasks(tasks)

# Вывод всех просроченных задач
display_overdue_tasks(tasks)