class Youtube:
    def __init__(self, username, subcribers = 0, subcriptions = 0):
        self.username = username
        self.subcribers = subcribers
        self.subcriptions = subcriptions

    def subcribe(self, user):
        user.subcribers += 1
        self.subcriptions += 1

    def get_number_subcribers(self):
        return f'User {self.username} subcribers: {self.subcribers}'
    
    def get_number_subcriptions(self):
        return f'User {self.username} subcriptions: {self.subcriptions}'
    

user1 = Youtube("Hung", 8)
user2 = Youtube("David")
user1.subcribe(user2)
user2.subcribe(user1)
print(user1.get_number_subcribers())
print(user2.get_number_subcribers())
print(user1.get_number_subcriptions())
print(user2.get_number_subcriptions())