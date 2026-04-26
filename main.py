class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Merhaba, ben {self.name}! {self.age} yaşındayım.")


user1 = User("Muhammet", 20)
user1.introduce()

# create a function that adds two numbers
def add_numbers(a, b):
    return a + b