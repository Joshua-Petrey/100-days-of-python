class Person:
	def __init__(self,name,age):
		self.name=name
		self.age = age
		self.followers = 0
		self.follows = 0

	def add_follows(self, username):
		self.follows += 1
		username.followers += 1
		

bob = Person("Bob", 65)
dave = Person("Dave", 45)

bob.add_follows(dave)
print(bob.name, bob.age, bob.follows)

