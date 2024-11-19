class Account:
    bank_name="State Bank of India"
    def __init__(self,balance,account_no):
        self.ac_balance=balance
        self.account_no= account_no
    
    def debit(self,amount):
        self.amount=amount
        if self.amount>self.ac_balance:
            print("Insufficient Amound")
        else:
            self.ac_balance -= self.amount
            print(f"You have succesfully withdraw amount: {self.amount},\n Your bank balance is {self.ac_balance} ")
    
    def Credit(self,de_amount):
        self.de_amount=de_amount
        self.ac_balance +=de_amount
        print(f"You have succesfully deposite your amount {self.de_amount},\n Your bank balance is {self.ac_balance} ")

cu=Account(30,2345)


while(True):
    print("Choose Option from given below")
    print("1. Bank Balance")
    print("2. Withdraw Amount")
    print("3. Deposite Amount")
    print("4. Exit")

    option=int(input("Enter your option: "))

    if(option==1):
        print(cu.ac_balance)
    elif(option==2):
        withdraw_amount=int(input("Enter the Amount you want to withdraw"))
        cu.debit(withdraw_amount)
    elif(option==3):
        deposite_amount = int(input("Enter the amount you want to depoiste"))
        cu.Credit(deposite_amount)
    else:
        print("Thanks for Visiting Us")
        break;



    

