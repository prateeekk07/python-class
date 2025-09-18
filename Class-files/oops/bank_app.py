# hdfc bank
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
    name = "HDFC Bank"
    def __init__(self, acc_num, name, acc_type, pin, bal=5000):
        self.acc_number = acc_num # TODO: random generate, use random library
        self.acc_type = acc_type
        self.name = name
        self.balance = bal
        self.atm_pin = pin
        self.acc_statement = []

    def show_details(self):
        print(f"""Account Number: {self.acc_number}
Account Holder Name: {self.name}
Account Type: {self.acc_type}
Account Balance: {self.balance}
""")
    
    def show_balance(self):
        print(f"Your available balance is: {self.balance}")

    def deposit(self, amt):
        self.balance += amt
        print("Amount deposited successfully!")
        self.acc_statement.append(f"Credit: {amt} - Balance: {self.balance}")
        self.show_balance()


    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amt
            print("Amount withdrawn successfully!")
            self.acc_statement.append(f"Debit: {amt} - Balance: {self.balance}")
            self.show_balance()

    def show_statement(self, num):
        for i in self.acc_statement:
            print(i)

    def update_pin(self, new_pin):
        if len(new_pin) != 4:
            print("New pin should be of 4 digits")
        else:
            self.atm_pin = new_pin
            print("New pin updated successfully!")
            
    # TODO: implement loan
    # TODO: last 5 statement


bank_obj = Bank(11224455, "Aditi", "Saving", 5481, 125000)
# bank_obj.show_details()
# bank_obj.show_balance()
# bank_obj.deposit(5000)
# bank_obj.withdraw(20000)
c = 0
while True:
    print(f"Welcome to {Bank.name}!")
    user_pin = int(input("Enter your pin:- "))
    if user_pin != bank_obj.atm_pin:
        print("Invalid pin.")
        break
    print("""########################
Choose an option:
SD - Show Details
B  - Show Balance
D  - Deposit
W  - Withdraw
ST - Statement
E  - Exit
          """)
    user_inp = input("Enter your choice:- ").upper() # SD
    if user_inp == "SD":
        bank_obj.show_details()
    elif user_inp == "B":
        bank_obj.show_balance()
    elif user_inp == "D":
        user_amt = int(input("Enter an amount to be deposited:-"))
        bank_obj.deposit(user_amt)
    elif user_inp == "W":
        user_amt = int(input("Enter an amount to be withdrawn:-"))
        bank_obj.withdraw(user_amt)
    elif user_inp == "ST":
        bank_obj.show_statement()
    elif user_inp == "E":
        print(f"Thank you for banking with {Bank.name}! Visit Again!")
        break
    else:
        c += 1
        if c == 3:
            print("Too many invalid attempts.")
            break
        print("Invalid option. Try again!")
