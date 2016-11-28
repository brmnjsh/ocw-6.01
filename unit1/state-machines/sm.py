class NN:
	def __init__(self):
		self.n = 0
	def get(self):
		self.n += 1 
		return str(self.n)
	def reset(self):
		self.n = 0 

class NS(NN):
	def get(self, s):
		return s + NN.get(self)

# foo = NS()
# print foo.get('a') 
# print foo.get('b')  
# foo.reset()
# print foo.get('c') 

class AccountPounds:
	def __init__(self, i):
		self.balance = i
	def depositPounds(self,i):
		self.balance = (self.balance + i) + ((self.balance + i) * .04)
		return self.balance

x = AccountPounds(1)
print x.depositPounds(1.5)

