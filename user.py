import json
import os
from pathlib import Path


# import itertools
class User:
    # id_iter = itertools.count()
    def __init__(self, username, password):
        # self.id = next(self.id_iter)
        self.username = username
        self.password = password

    def __str__(self):
        return (f"Username : {self.username}\n"
                f"Password : {self.password}\n")

    def registerUserList(self):
        # Opening JSON file
        userListFile = open('UserData/userInfoList.json', 'w')
        user_array = json.load(userListFile)
        print(user_array)
        userListFile.close()
        userListFile = open('UserData/userInfoList.json', 'w')

        userData = {
            'username': f'{self.username}',
            'password': f'{self.password}',
        }
        usernameExists = False
        for user_item in user_array:
            if userData['username'] == user_item['username']: usernameExists = True

        else:
            user_array.append(userData)
            userListObject = json.dumps(user_array)
            userListFile.write(userListObject)
            userListFile.close()

        return usernameExists


