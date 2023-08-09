import json
import datetime

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
        userData = {
            'username': f'{self.username}',
            'password': f'{self.password}',
        }
        usernameExists = False

        with open('UserData/userInfoList.json') as userListFile:
            user_array = json.load(userListFile)

        for user_item in user_array:
            if userData['username'] == user_item['username']:
                usernameExists = True

        if not usernameExists:
            user_array.append(userData)
            with open('UserData/userInfoList.json', 'w') as userListFile:
                userListFile.write(json.dumps(user_array))
            open(f'UserData/Users/{self.username}.json', 'x')

        return usernameExists

    def userLoginFile(self):
        with open('UserData/userInfoList.json') as userListFile:
            user_array = json.load(userListFile)

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

    def userDataRetriever(self):
        with open(f'UserData/Users/{self.username}.json') as userRecordsFile:
            sessionRecords = json.load(userRecordsFile)

        return sessionRecords

    def userDataRecorder(self, numberofgames, numberofvictories):
        currentDatetime = datetime.datetime.now()
        currentDay = currentDatetime.day
        sessionData = {
            'Date': currentDay,
            'Number_of_games': numberofgames,
            'Number of victories': numberofvictories
        }
        userRecordsFile = open(f'UserData/Users/{self.username}.json')
        fileLength = len(userRecordsFile.read())
        print(fileLength)
        userRecordsFile.close()
        if fileLength > 0:
            with open(f'UserData/Users/{self.username}.json') as userRecordsFile:
                sessionRecords = json.load(userRecordsFile)

            sessionRecords.append(sessionData)
            with open(f'UserData/Users/{self.username}.json', 'w') as userRecordsFile:
                userRecordsFile.write(json.dumps(sessionRecords))
        else:
            sessionDataArray = [sessionData]
            with open(f'UserData/Users/{self.username}.json', 'w') as userRecordsFile:
                userRecordsFile.write(json.dumps(sessionDataArray))
