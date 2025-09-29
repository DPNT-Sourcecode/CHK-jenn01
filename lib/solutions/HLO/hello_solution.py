
class HelloSolution:
    
    # friend_name = Unicode string
    def hello(self, friend_name):
        if not friend_name:
            raise ValueError("Please provide friend name")
        elif not isinstance(friend_name, str):
            raise ValueError("Please give a friend name as a string")
        else:
            return "Hello, " + friend_name + "!"
