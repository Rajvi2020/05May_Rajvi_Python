class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers


inf = Influencer("rajvi123", "rajvi@gmail.com", 50000)


print("Username:", inf.username)
print("Email:", inf.email)
print("Followers:", inf.followers)