

tasks = []

def create_task(task: dict):
  new_task = {
    "id": max((t['id'] for t in tasks), default=0) + 1,
    **task
  }

  tasks.append(new_task)
  return new_task

def get_all_task():
  return tasks


def get_task_by_id(task_id:int):
  for task in tasks:
    if task['id'] == task_id:
      return task
  return None

def update_task(task_id:int, updated_task:dict):
  task = get_task_by_id(task_id)

  if task == None:
    return None

  task.update(updated_task)
  return task


def delete_task(task_id:int):

  task = get_task_by_id(task_id)

  if task == None:
    return None

  tasks.remove(task)
  return task