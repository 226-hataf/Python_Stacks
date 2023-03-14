import requests
import json
from api.models import Student

url = "http://127.0.0.1:8000/api/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=url, data=json_data)
    data = r.json()
    #return datacls
    
    #print(data)

    #print(get_data())

#get_data(1)


def post_data():
    
    data= {
        'name':'Kainat',
        'roll':230,
        'city':'Karachi',
    }
    
    json_data= json.dumps(data)
    r = requests.post(url=url,data = json_data)
    data = r.json()
    
    print(data)  
post_data()


def update_data():
    
    data= {
        'id': 3,  
        'name':'hataf',
       # 'roll':226,
        'city':'Lahore',
    }
    
    json_data= json.dumps(data)
    r = requests.put(url=url,data = json_data)
    data = r.json()
    
  #  print(data)  
#update_data()

# def delete_data():
    
#     data= { 'id': 7}
    
#     json_data= json.dumps(data)
#     r = requests.delete(url=url,data = json_data)
#     data = r.json()
    
# delete_data()

# def delete_data():
#     student_data = {
#         'id': 6
#     }
#     json_data = json.dumps(student_data)
#     stud_obj =student.objects.delete(url=url, data=json_data)
#     data = stud_obj.json()
#     print(data)


# delete_data()
