class User:
    def __init__(self, username, password, profile_picture):
        self.username = username
        self.password = password
        self.profile_picture = profile_picture

    def greet(self):
        print("Hallo " + self.username + " nice to meet you.")

johanna = User("Johanna", "23095q2po4i5bsöeogb", "profile_picture")
johanna.greet()