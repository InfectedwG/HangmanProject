class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return (f"Username : {self.username}\n"
                f"Password : {self.password}\n")

    def registerUserList(self):
        filePath = 'C:/Users/maxim/Desktop/Projet1.4/HangmanProject/UserData/userList.txt'
        userList = open(filePath, 'a')
        userList.write(self.__str__())