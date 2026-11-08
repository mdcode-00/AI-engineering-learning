"function and arguments.....///////"


def calculate_total(price, quantity):
    total = price * quantity
    return total

print(calculate_total(10, 5))


# "position argument"

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Alice", 30)  # Positional arguments


# keyword arguments

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(age=30, name="Alice")  # Keyword arguments


# default arguments

def greet(name, age=25):
    print(f"Hello {name}, you are {age} years old.")

greet("Alice")  # Default argument for age

# 2 *args and **kwargs

def calculate_total(*numbers):
  return sum(numbers)

print(calculate_total(10, 5, 3))  # Output: 18

# **kwargs
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


print_info(name="Alice", age=30, city="New York")


# type hints

def calculate_total(price: float, quantity: int) -> float:
    total = price * quantity
    return total


def get_task_title(tasks: list[dict]) -> list[str]:
    title = []

    for task in tasks:
        title.append(task["title"])
    return title

print(get_task_title([{"title": "Task 1"}, {"title": "Task 2"}]))  # Output: ['Task 1', 'Task 2']

def find_task_by_id(tasks: list[dict], task_id: int) -> dict | None:
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

print(find_task_by_id([{"id": 1, "title": "Task 1"}, {"id": 2, "title": "Task 2"}], 2))  # Output: {'id': 2, 'title': 'Task 2'}
print(find_task_by_id([{"id": 1, "title": "Task 1"}, {"id": 2, "title": "Task 2"}], 3))  # Output: None



