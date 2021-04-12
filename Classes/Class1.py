# Creating your own class - Use Class key work
# Empty class - use pass
class User:
    # initialize
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # not all attritubes need to be initialized
        self.follwers = 0


# Assigning user2 to the User class
# we need to initialize the user attributes
user2 = User("002", "John B")

# Print user2
print(user2)
print(user2.username)
print(user2.id)

user3 = User("003", "Katie")

# Followers is set to 0 so 0 will be printed here
print(user3.follwers)


## Assigning Class to an object without initializing
# user1 = User()
## Assigning object to an attribute - Attribute is a Variable related to an Object
## .id is the variable and user1 is the object
# user1.id = "001"