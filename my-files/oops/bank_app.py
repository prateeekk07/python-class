# PNB bank
# acc holder
    # - name
    # - account number
    # - balance
    # - type of account
# deposit
# withdraw
# balance check
# loan
# new pin set
# statement

class Bank:
    name = "PNB Bank"
    def __init__(self,acc_num,name,acc_type, bal=500):
        self.acc_name = acc_num
        self.name = name
        self.acc_type = acc_type
        self.balance = bal

    def show_details(self):
        print(f"""Account Number: {self.acc_name}
Account Holder Name: {self.name}
Account Type: {self.acc_type}
Account Balance: {self.balance}
"""
        )
    
    def show_balance(self):
        print(f"Your Current Balance is: {self.balance}")        

    def deposit(self,amt):
        self.balance += amt
        print("Amount Deposited Succesfully")
        self.show_balance()
        

    def withdraw(self,amt):
        self.balance -= amt
        print("Amount withdraw Succesfully")
        self.show_balance()


bank_obj = Bank(1122334455,"Prateek","Saving",5000)
bank_obj.show_balance()        
bank_obj.deposit(500)
bank_obj.withdraw(1000)
