# for loop
users = {'hans':'active','more':'inactive'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        print(user,status)

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        print(user,status)
