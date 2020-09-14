class User():
    name = ''
    age = ''
    major = ''

    def init(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_major(self):    
        return self.major 
        
user1 = User()
user1.init('배성현', '25', '경영정보학과') 

print(user1.get_name())
print(user1.get_age())
print(user1.get_major())


