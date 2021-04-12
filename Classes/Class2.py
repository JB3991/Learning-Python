class User2:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

# Adding a method to the class
    def follow(self, user):
        # add 1 if the user has a follower
        user.followers += 1
        # Add one to self if i start following a user
        self.following += 1


user1 = User2("001", "Chris")
user2 = User2("002", "Joe")

# User1 is now following user2
user1.follow(user2)

# print users Followers and Following
print(user1.followers)
print(user1.following)

print(user2.followers)
print(user2.following)
