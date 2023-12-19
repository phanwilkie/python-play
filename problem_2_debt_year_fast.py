#Calculates the minimum fixed monthly payment needed in order pay off a credit card 
#balance within 12 months. 
#By a fixed monthly payment, we mean a single number which does not change each month, 
#but instead is a constant amount that will be paid each month.

balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12.0

monthlyPaymentLowerBound = balance/12.0
monthlyPaymentHigherBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
#monthlyPaymentMiddleBound  = (monthlyPaymentLowerBound + monthlyPaymentHigherBound) / 2
monthlyPaymentMiddleBound = 29157.09
remainingBalance = balance

#while total remaining is greater than 0.01
while remainingBalance < -0.01 or remainingBalance > 0.01:
	remainingBalance = balance

	#print monthlyPaymentLowerBound
	#print monthlyPaymentHigherBound
	#print monthlyPaymentMiddleBound

	print 'For monthly payment of $' + str(round(monthlyPaymentMiddleBound))

	for i in range(1,13):
		#pay the monthly payment
		remainingBalance -= monthlyPaymentMiddleBound
		#add interest to the remaining balance
		remainingBalance = remainingBalance + (remainingBalance * monthlyInterestRate)
		print 'Month: ' + str(i) + ' | Remaining Balance: $' + str(round(remainingBalance,2))

	print ''
	print 'Total remaining: ' + str(round(remainingBalance,2))
	print ''

	#update the lower and upper bound depending on the total remaining:
	if remainingBalance < 0:
		#print 'go lower'
		monthlyPaymentHigherBound = monthlyPaymentMiddleBound
		monthlyPaymentMiddleBound = (monthlyPaymentLowerBound + monthlyPaymentMiddleBound)/2
		#print monthlyPaymentLowerBound
		#print monthlyPaymentHigherBound
		#print monthlyPaymentMiddleBound

	else:
		#print 'go higher'
		monthlyPaymentLowerBound = monthlyPaymentMiddleBound
		monthlyPaymentMiddleBound = (monthlyPaymentHigherBound + monthlyPaymentMiddleBound)/2
		#print monthlyPaymentLowerBound
		#print monthlyPaymentHigherBound
		#print monthlyPaymentMiddleBound