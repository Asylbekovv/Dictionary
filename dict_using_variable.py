user1_name = 'Arstan'
user1_id = 1
user1_password = 'Arscher_009renga'

user2_name = 'John'
user2_id = 2
user2_password = 'Team0012_Asqw'

user1_dict = {
    'name': user1_name,
    'id': user1_id,
    'password': user1_password
}

user2_dict = {
    'name': user2_name,
    'id': user2_id,
    'password': user2_password
}

print(user1_dict, user2_dict)
print(len(user1_dict))
print(type(user1_name))
print(user2_dict.get('id'))
print(user1_dict.get('password'))

my_dict = {}
print(my_dict.__doc__)
