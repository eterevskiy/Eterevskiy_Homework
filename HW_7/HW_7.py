import csv
import json
import requests

# with open(r"HW_7\todos.json","r") as file :
#     todos = json.load(file)

# with open(r"HW_7\users.json","r") as file :
#     users = json.load(file)

todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
users = requests.get('https://jsonplaceholder.typicode.com/users').json()

for user in users :
    with open(rf"HW_7\users_info\{user['name']}.csv",'w') as file :
        writer = csv.writer(file, delimiter = ",")
        writer.writerow(["id","title","completed"])
        for todo in todos :
            if todo['userId']==user['id'] :
                    writer.writerow(list(todo.values())[1:])


        
    
  