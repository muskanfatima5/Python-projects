import click
import json
import os

TODO_FILE = "todo.json"

def load_todo():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_todo(todo):
    with open(TODO_FILE, "w") as file:
        json.dump(todo, file, indent=4)

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    todo = load_todo()
    todo.append({"task": task, "done": False})  
    save_todo(todo)
    click.echo(f"Task added: {task}")

@click.command() 
def list():
    """List all the tasks"""
    todos = load_todo()
    if not todos:
        click.echo("No tasks found")
        return

    for index, task in enumerate(todos, 1):
        status = "✔" if task["done"] else "✘"
        click.echo(f"{index}. {task['task']} [{status}]")

@click.command() 
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as completed"""
    todos = load_todo()
    if 0 < task_number <= len(todos):
        todos[task_number - 1]['done'] = True
        save_todo(todos)
        click.echo(f"Task {task_number} is completed")
    else:
        click.echo(f"Task {task_number} not found")

@click.command()
@click.argument("task_number", type=int)
def delete(task_number):
    """ Delete a task from the list"""
    todos = load_todo()
    if 0 < task_number <= len(todos):
        deleted_task = todos.pop(task_number - 1)  
        save_todo(todos)
        click.echo(f"Deleted Task: {deleted_task['task']}")
    else:
        click.echo(f"Task {task_number} not found")

cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)

if __name__ == "__main__":
    cli()
