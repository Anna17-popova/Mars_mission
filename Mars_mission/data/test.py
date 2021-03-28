from requests import post, get, delete

print(get('http://localhost:8070/api/v2/user').json())
print(get('http://localhost:8070/api/v2/user/3').json())
#пользователя с id 999 нет в базе данных
print(get('http://localhost:8070/api/v2/user/999').json())
#пустой запрос
print(post('http://localhost:8070/api/v2/user').json())
#запрос с недостаточным количеством параметров
print(post('http://localhost:8070/api/v2/user', json={'name': 'Anna', 'surname': 'Popova'}).json())
#корректный запрос
print(post('http://localhost:8070/api/v2/user', json={'name': 'Harry', 'surname': 'Potter', 'address': 'module_4', 'age': 17,
                                                      'position': '-', 'speciality': '-', 'email': '123@mars.tru'}).json())
#пользователя с id 999 нет в базе данных
print(delete('http://localhost:8070/api/v2/user/999').json())
print(delete('http://localhost:8070/api/v2/user/3').json())
