
from operator import le


class TaskAssistant:
  def __init__(self):
    self.tasks = []

  def add_task(self, title: str, priority: str = "medium") -> bool:
    valid = ["high", "low", "medium"]

    if priority not in valid:
        return False
    
    self.tasks.append({
       "title": title,
       "priority": priority,
          "status": "pending"
       })

    return True

  def update_task(self, index , title: str) -> bool:
        if not (0 <= index < len(self.tasks)):
          return False

        self.tasks[index]["title"] = title
        return True

  def complete_task(self, index ) -> bool:
     if not (0 <= index < len(self.tasks)):
        return False

     self.tasks[index]["status"] = "completed"
     return True

  def delete_task(self , index) -> bool:
     if not (0 <= index < len(self.tasks)):
        return False

     del self.tasks[index]
     return True 

  def get_tasks_by_priority(self,priority) -> list[dict]:
     
     pri = []

     for task in self.tasks:
        if task["priority"] == priority:
           pri.append(task)

     return pri

  def pending_task(self) -> list[dict]:
     pending = []

     for task in self.tasks:
             if task["status"] == "pending":
                pending.append(task)
     return pending

  def summary_task(self) -> dict | None:
       
       total = len(self.tasks)
       completed = 0
       pending = 0

       for task in self.tasks:
          if task["status"] == "completed":
            completed +=1

          if task["status"] == "pending":
             pending += 1

       return {
          "total" : total,
          "complete": completed,
          "pending": pending
       }      
     
  def get_task(self) -> list[dict]:

    for index , task in enumerate(self.tasks): 
     print(
        f"{index}. {task['title']} | "
        f"{task["priority"]} | {task["status"]}"
     )


