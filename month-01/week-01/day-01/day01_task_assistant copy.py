"""A tiny Day 1 assistant that helps you define one focused task."""



# class TaskAssistant:
#     def __init__(self):
#         self.tasks = []


#     def add_task(self, title: str, priority: str = "medium"):
#         valid = ["low", "medium", "high"]

#         if priority not in valid:
#             return False

#         task = {
#             "title": title,
#             "priority": priority,
#             "status": "pending"
#         }

#         self.tasks.append(task)
#         return True

#     def complete_task(self, index: int):
#         if 0 <= index < len(self.tasks):
#             self.tasks[index]["status"] = "completed"
#             return True

#         return False

#     def pending_task(self):
#         pending = []

#         for task in self.tasks: 
#          if task['status'] == "pending":
#             pending.append(task["title"])
#         return pending


#     def count_complete_task(self):
#         count = 0
#         for task in self.tasks:
#             if task['status'] == "completed":
#                 count += 1
#         return count    

#     def update_task(self, index: int, new_tital: str):
#             if 0<= index < len(self.tasks):
#                 self.tasks[index]["title"] = new_tital
#                 return True
#             return False

#     def get_by_perority(self,priority: str):
#        valid = ["low", "medium", "high"]

#        if priority not in valid:
#          return []

#        result = []

#        for task in self.tasks:
#         if task["priority"] == priority:
#             result.append(task)

#        return result


#     def delete_task(self, index: int):
#         if 0 <= index < len(self.tasks):
#             # self.tasks.remove(self.tasks[index]) better pattern
#             del self.tasks[index]
#             return True
        
#         return False

#     def summary_task(self):

#         total = len(self.tasks)
#         completed = self.count_complete_task()
#         pending = len(self.pending_task())

#         return {
#             "total": total,
#             "completed": completed,
#             "pending" : pending
#         }


#     def show_tasks(self):
#         for index, task in enumerate(self.tasks):  
#              print(
#                 f"{index}. {task['title']} | "
#                 f"{task['priority']} | {task['status']}"
#             )


# assistant = TaskAssistant()

# assistant.add_task("Study FastAPI", "medium")
# assistant.add_task("Learn Python", "high")
# assistant.add_task("Build an AI application", "ggg")
# assistant.add_task("Build an AI application", "high")

# assistant.complete_task(0)
# assistant.delete_task(1)
# assistant.update_task(0,"Updated")
# assistant.get_by_perority("high")
# print("Pending:", assistant.pending_task())
# print("Completed:", assistant.count_complete_task())
# print("Summary:", assistant.summary_task())


# # Update task
# assert assistant.update_task(0, "Learn Python deeply") == True
# assert assistant.update_task(100, "Invalid task") == False

# # Filter by priority
# assert len(assistant.get_by_perority("high")) >= 0
# assert assistant.get_by_perority("urgent") == []

# # Delete task
# assert assistant.delete_task(0) == True
# assert assistant.delete_task(100) == False

# print("All tests passed!")

# assistant.show_tasks()

# "day one completed...."

# revision


class TaskAssistant:

    def __init__(self):

        self.tasks = []

    def add_task(self,title:str, priority: str = "medium"):
        if title == '':
            return False

        valid = ["medium" , "low" , "high"]

        if priority not in valid :
            return False        

        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "priority": priority,
            "status": "pending"
        }

        self.tasks.append(task)
        return True


    def complete_task(self,task_id):
        if 0 <= task_id < len(self.tasks):
            return False
    

        for task in self.tasks:
           if task["id"] == task_id:
               task["status"] = "completed"
               return True
        
        return False


    def delete_task(self,task_id):

        for task in self.tasks:
         if task["id"] == task_id:
            self.tasks.remove(task)
            return True
                
        return False

    def get_pending(self):
        pen = []

        for task in self.tasks:
            if task["status"] == "pending":
                pen.append(task["title"])

        return pen

    def get_complete_count(self):
        count = 0

        for task in self.tasks:
            if task["status"] == "completed":
                count += 1

        return count

    def update_task(self ,task_id, new_title):
        for task in self.tasks:
            if task["id"] == task_id:
                task["title"] = new_title
                return True
        return False 

    def get_tasks_by_priority(self, priority):

        pre = []

        for task in self.tasks:
            if task["priority"] == priority:
                pre.append(task["title"])
        return pre        


    def show_task(self):
        for task in self.tasks:
            print(
                f"{task["id"]}. {task["title"]} | "
                f"{task["priority"]} | {task["status"]}"
            )


ass = TaskAssistant()

ass.add_task("Learning python")
ass.add_task("Learning nothing")
ass.add_task("Learning DSA" , "low")
ass.add_task("")
ass.add_task("Learning js")
ass.complete_task(3)
ass.delete_task(2)
print("Pending Task",ass.get_pending())
print("complete Task",ass.get_complete_count())
print(ass.update_task(1, "Learn Python deeply"))
print(ass.update_task(100, "Invalid task"))
print("preority", ass.get_tasks_by_priority("low"))



ass.show_task()

