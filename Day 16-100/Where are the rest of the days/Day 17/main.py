class User:

    def __init__(self, user_id, username):
        print("i am being created!")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "daniel")
user2 = User("002", "daniel2")

print(user1.id)
print(user1.followers)

user1.follow(user2)

print(user1.following)
print(user2.followers)
print(user2.following)
print(user1.followers)
