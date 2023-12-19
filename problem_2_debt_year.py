#Calculates the minimum fixed monthly payment needed in order pay off a credit card 
#balance within 12 months. 
#By a fixed monthly payment, we mean a single number which does not change each month, 
#but instead is a constant amount that will be paid each month.

balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12.0

monthlyPayment = 0.0
remainingBalance = balance

#1. Start with $10 and see whether it pays off the debt after 12 months...
while remainingBalance > 0:
	remainingBalance = balance	
	monthlyPayment += 10
	print 'For monthly payment of $' + str(monthlyPayment)

	for i in range(1,13):
		#pay the monthly payment
		remainingBalance -= monthlyPayment
		#add interest to the remaining balance
		remainingBalance = remainingBalance + (remainingBalance * monthlyInterestRate)
		print 'Month: ' + str(i) + ' | Remaining Balance: $' + str(round(remainingBalance,2))

	print ''
	print 'Total remaining: ' + str(round(remainingBalance,2))
	print ''

print 'Lowest Payment: ' + str(monthlyPayment)
