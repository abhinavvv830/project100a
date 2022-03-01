class Atm(object):
    def __init__(self,atmcardnumber,pinnumber,CashWithdrawl, BalanceEnquiry):
        self.atmcardnumber=atmcardnumber
        self.pinnumber=pinnumber
        self.CashWithdrawl=CashWithdrawl
        self.BalanceEnquiry=BalanceEnquiry
    
    def bankbalance(self,amount):
        print("400000")
    def withdraw(self):
        print("enter the required amount") 
           
HDFC=Atm("123876","500","4000","no data")
print(HDFC.atmcardnumber)
print(HDFC.pinnumber)
print(HDFC.CashWithdrawl)
print(HDFC.bankbalance(400000))
print(HDFC.BalanceEnquiry)
print(HDFC.withdraw())    
    
    