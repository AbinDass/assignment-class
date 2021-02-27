class Bankaccount:
	def __init__ (self) :
		self.balance = 0

	def deposit (self) :
		amount = float (input ( "enter amount deposited : " )) 
		self.balance += amount 
		print ("\nAmount Deposited : ", amount) 

	def withdraw (self) :
		amount = float (input ( "enter amount withdrawed : " )) 
		if self.balance >= amount :
			self.balance = self.balance - amount 
			print ("\n Amount withdrawed : ", amount)
		else :
			print ("\n Insuficiant Balance ")

	def display (self):
		print ("\n available balance is : ",self.balance) 

a = Bankaccount () 
a . deposit () 
a . withdraw () 
a . display () 





# class Bank_Account: 
#     def __init__(self): 
#         self.balance=0
#         print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 
  
#     def deposit(self): 
#         amount=float(input("Enter amount to be Deposited: ")) 
#         self.balance += amount 
#         print("\n Amount Deposited:",amount) 
  
#     def withdraw(self): 
#         amount = float(input("Enter amount to be Withdrawn: ")) 
#         if self.balance>=amount: 
#             self.balance-=amount 
#             print("\n You Withdrew:", amount) 
#         else: 
#             print("\n Insufficient balance  ") 
  
#     def display(self): 
#         print("\n Net Available Balance=",self.balance) 
  
# # Driver code 
   
# # creating an object of class 
# s = Bank_Account() 
   
# # Calling functions with that class object 
# s.deposit() 
# s.withdraw() 
# s.display() 