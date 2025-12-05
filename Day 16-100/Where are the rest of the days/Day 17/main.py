class User:

    def __init__(self, user_id, username):
        print("i am being created!")
        self.id = user_id
        self.username = username
        self.followers = 0


user1 = User("001", "daniel")

print(user1.id)
print(user1.followers)
