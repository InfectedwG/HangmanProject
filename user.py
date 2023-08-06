class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return (f"Username : {self.username}\n"
                f"Password : {self.password}\n")