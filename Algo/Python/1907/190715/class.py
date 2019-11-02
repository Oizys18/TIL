class Service:
	secret = "A1"
	def setname(self, name):
		self.name = name
	def sum(self, a, b):
		result = a + b
		print("Mr.%s, The outcome of %s plus %s is %s." %(self.name, a, b, result))
       
pey = Service()
pey.setname("LAMA")
pey.sum(25,46)
print(pey.secret)



print("hello world")
