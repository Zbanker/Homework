import requests

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

user_input = int(input('Introduceti id-ul cautat: '))
if response.status_code == 200:
    posts = response.json()
    usr = {user_post['id'] : user_post for user_post in posts}
    print(f'User`s input:', usr[user_input])
    print(f'Posts userId:', usr[user_input]['userId'])
    print(f'Posts title:', usr[user_input]['title'])
    print(f'Posts id:', usr[user_input]['id'])
    print(f'Posts body:', usr[user_input]['body'])