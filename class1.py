class string ():
	def __init__ (self):
		self.str = ""

	def getstring (self):
		self.str = input("enter the string:   " )

	def printstring (self):
		print (self.str.upper ())


str = string ()
str.getstring () 
str.printstring ()