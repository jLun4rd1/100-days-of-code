# REMOVE COMMENT TO SEE NOTES CLEARLY!!

#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#|

# # How to create a class:
# class User:
#     def __init__(self, user_id, username):
#     # initialize attributes
#         print("New user being created...")
#         self.id = user_id
#         self.username = username
#         pass

# user_1 = User(user_id='001', username='juaum')
# # How to add an attribute:
# # user_1.id = '001'
# # user_1.username = 'juaum'
# print(user_1.username)

# # user_2 = User()
# # user_2.id = '002'
# # user_2.username = 'joana'

# # print(user_2.username)

#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#|

# # Final version:
# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         # default value parameter

# user_1 = User('001', 'juaum')
# user_2 = User('002', 'joana')

#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#|

# # Creating a method:
# class Car:
#     def __init__(self, seats):
#         self.seats = seats
    
#     def enter_race_mode(self):
#         self.seats = 2

#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#|

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1
        

user_1 = User('001', 'juaum')
user_2 = User('002', 'joana')

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)
