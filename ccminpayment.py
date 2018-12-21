total_paid=0
for month in range (1,13):
    print ("Month:" + str(month))
    minimum_payment = round((balance * monthlyPaymentRate),2)
    print ("Minimum monthly payment:" + str(minimum_payment))
    balance = (balance - minimum_payment)
    balance = round( (balance * (annualInterestRate/12) + balance), 2)
    print ("Remaining balance:" +str (balance))
    total_paid += minimum_payment
print ("Total paid:" + str(total_paid))
print ("Remaining balance:" +str(balance))
