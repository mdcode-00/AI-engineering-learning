import requests
import json

url = "https://jsonplaceholder.typicode.com/users"
postURL = "https://jsonplaceholder.typicode.com/posts"


# get data
response = requests.get(url , timeout=10)

# print(response.status_code)
# print(response.json())

users = response.json()

# for user in users:
#   print(f"name: {user["name"]}\nemail: {user["email"]}")

#  post data

data = {
    "title": "Learning Python",
    "body": "I am practicing APIs.",
    "userId": 1
}


response = requests.post(postURL , json=data , timeout=10)

# print(response.status_code)
# print(response.json())




# try:
#     response = requests.get(url, timeout=10)
#     response.raise_for_status()

#     print(f"Users: {response.json()}")

# except requests.exceptions.Timeout:
#     print("Request timed out.")

# except requests.exceptions.ConnectionError:
#     print("Internet connection error.")

# except requests.exceptions.HTTPError:
#     print("API returned an HTTP error!")

# except requests.exceptions.RequestException:
#     print("Something went wrong with the request.")


# def divide_numbers() -> None:
#   try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter first number: "))

#     result = a / b

#   except ValueError:
#     print("write valid number!")

#   except ZeroDivisionError:
#     print("Second number shouldn't be zero!")

#   else:
#     print("Result:", result)

#   finally:
#     print("Program is ended!")

# divide_numbers()


# def check_age() -> None:

#  try:
#   age = int(input("enter your age: "))

#   if age < 18:
#    print("Age must be 18 or above.")

#   else:
#    print("Eligible")

#  except ValueError: 
#    print("enter valid number!")

#  finally:
#    print("process end")

 
# check_age()

def create_task(title: str) -> dict:

    if not title.strip():
        raise ValueError("Task title cannot be empty!")

    return {
        "title": title,
        "status": "pending"
    }


result = create_task("Learn Python")
print(result)