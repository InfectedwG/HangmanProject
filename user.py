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
        userListFile = open('UserData/userInfoList.json')
        user_array = json.load(userListFile)
        userListFile.close()

        userListFile = open('UserData/userInfoList.json', 'w')
        userData = {
            'username': f'{self.username}',
            'password': f'{self.password}',
        }
        usernameExists = False
        for user_item in user_array:
            if userData['username'] == user_item['username']:
                usernameExists = True
        if not usernameExists:
            user_array.append(userData)
            userListObject = json.dumps(user_array)
            userListFile.write(userListObject)

        userListFile.close()

        return usernameExists

    def userLoginFile(self):
        userListFile = open('UserData/userInfoList.json')
        user_array = json.load(userListFile)
        userListFile.close()

        userData = {
            'username': f'{self.username}',
            'password': f'{self.password}',
        }
        loginAllow = False
        for user_item in user_array:
            if userData == user_item:
                loginAllow = True
                break

        return loginAllow
