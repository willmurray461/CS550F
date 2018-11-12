import random

class Account:
	def __init__(self,account_type,username,password):
		self.account_type = account_type
		self.password = password
		self.balance = 0
		self.account_number = random.randrange(1000000000000000,10000000000000000)
	def check_balance(self):
		return "Your Balance is: $"+str(self.balance)
	def deposit(self,amount):
		amount = amount*100
		amount = amount//1
		amount = amount/100
		if amount <= 0.01:
			return "You cannot deposit a sum less than $0.01"
		else:
			self.balance = self.balance + amount
			return "Added $"+str(amount)+" to account number "+str(self.account_number)+"."
	def withdraw(self,amount):
		amount = amount*100
		amount = amount//1
		amount = amount/100
		if amount > self.balance:
			return "Your maximum withdrawal is $"+str(self.balance)
		elif amount < 0.01:
			return "You cannot withdraw a sum less than $0.01"
		else:
			self.balance = self.balance - amount
			return "$"+str(amount)+" was withdrawn form account number "+str(self.account_number)+"."
	def log_in(self,username,password):
		if password == self.password and username == self.username:
			return "Account Number: "+str(self.account_number)+"\nAccount Type: "+str(self.account_type)+"\nBalance: $"+str(self.balance)
		else:
			return "Incorrect Username or Password"

Account1 = Account("Checking","Bob","1234")
print(Account1.log_in("Bob","1234"))
print(Account1.deposit(500000))
print(Account1.deposit(-1))
print(Account1.withdraw(27000))
print(Account1.withdraw(-1))
print(Account1.check_balance())


