#balance = 999999
original_balance=balance
#annualInterestRate=0.18
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
print ("Lowest Payment:" + str(minimum_monthly_payment))
