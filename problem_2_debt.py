#Calculates the minimum fixed monthly payment needed in order pay off a credit card 
#balance within 12 months. 
#By a fixed monthly payment, we mean a single number which does not change each month, 
#but instead is a constant amount that will be paid each month.

balance = 320000
monthlyPaymentRate = 0.04
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
minimumPayment = monthlyPaymentRate * balance
totalPaid = 0
#monthlyInterest = (balance - minimumPayment) * (annualInterestRate/12)

#1. For each month, workout the monthly amount required to pay the remaining balance
for i in range(0,13):
	if i+1 != 13:
		print 'Month: ' + str(i+1)
		print 'Minimum monthly payment: ' + str(round(minimumPayment, 2))
		balance = (balance - minimumPayment)
		totalPaid += minimumPayment
		balance = balance + (balance * monthlyInterestRate)
		minimumPayment = monthlyPaymentRate * balance
		print 'Remaining balance: ' + str(round(balance, 2))
		print ''
	else:
		print 'Total Paid: ' +str(round(totalPaid, 2))
		print 'Remaining balance: ' + str(round(balance, 2))
