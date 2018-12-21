#balance = 3926
original_balance=balance
#annualInterestRate=0.2
minimum_monthly_payment = balance / 12
interest_free_balance=balance
while (balance !=0):    
        for i in range (1,13):
                #print ("Minimum monthly payment in while loop:" + str(minimum_monthly_payment))
                interest_free_balance = round ((balance - minimum_monthly_payment),2)
                balance = round(interest_free_balance + (interest_free_balance * (annualInterestRate / 12)),2)
                if ( i == 12 and balance < 0):
                        if (int(balance) == 0):
                                balance = 0
                                break
                        #print ("Balance has fallen below zero:" +str (balance))
                        adjustment = round(abs((balance)/ 12),2)
                        balance = original_balance
                        minimum_monthly_payment -= adjustment
                        #print adjustment
                elif (i == 12 and balance > 0):
                        if (int(balance) == 0):
                                balance = 0;
                                break
                        #print ("Balance has gone above zero:" +str (balance))
                        adjustment = round(balance / 12,2)
                        balance = original_balance
                        minimum_monthly_payment += adjustment
while (int(minimum_monthly_payment) % 10 != 0):
        minimum_monthly_payment += 0.01

minimum_monthly_payment = int(minimum_monthly_payment)
print ("Lowest Payment:" + str(minimum_monthly_payment))

