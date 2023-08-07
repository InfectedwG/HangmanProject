import json


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
        filePath = 'C:/Users/maxim/Desktop/Projet1.4/HangmanProject/UserData/userInfoList.json'
        userListFile = open(filePath)
        # extract data in json file
        user_array = json.load(userListFile)
        userListFile.close()
        userListFile = open(filePath, 'w')

        userData = {
            'username': f'{self.username}',
            'password': f'{self.password}',
        }
        usernameExists = False
        for user_item in user_array:
            if userData['username'] == user_item['username']: usernameExists = True

        if usernameExists: self.registerUserList()
        else:
            user_array.append(userData)
            userListObject = json.dumps(user_array)
            userListFile.write(userListObject)
            userListFile.close()


