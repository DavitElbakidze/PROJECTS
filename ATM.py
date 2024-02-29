import os

class ATM:
    def __init__(self):
        # ამოწმებს არსებობს თუ არა 'accounts.txt' ფაილი. თუ არ არსებობს ქმნის.
        if not os.path.isfile('accounts.txt'):
            self.create_accounts_file()
        # ტვირთავს მომხმარებლების ანგარიშებს ფაილიდან როდესაც ობიექტი შეიქმნება
        self.accounts = self.load_accounts()

    def load_accounts(self):
        # კითხულობს მომხმარებლების ანგარიშებს ფაილიდან და აბრუნებს ლექსიკონის სახით
        accounts = {}
        with open('accounts.txt', 'r') as file:
            for line in file:
                parts = line.strip().split()
                pin = parts[0].split(":")[1]
                amount = float(parts[1].split(":")[1])
                username = " ".join(parts[2:]).split(":")[1]
                 # ინახავს ანგარიშების ინფორმაციას ლექსიკონში
                accounts[pin] = {'balance': amount, 'username': username}
        return accounts

    def save_accounts(self):
        # წერს მომხმარებლების ანგარიშებს ფაილში
        with open('accounts.txt', 'w') as file:
            for pin, info in self.accounts.items():
                file.write(f"pin:{pin} amount:{info['balance']} user:{info['username']}\n")

    def create_accounts_file(self):
        # ტექსტური ფაილის შექმნა

        with open('accounts.txt', 'w') as file:
            # ქმნის კონკრეტული მომხმარებლების ანგარიშებს
            file.write("pin:1234 amount:1250.0 user:Davit Elbakidze\n")
            file.write("pin:5678 amount:1500.0 user:Step Academy\n")

    def check_balance(self, pin):
        # აბრუნებს ბალანსს
        return self.accounts[pin]['balance']

    def withdraw(self, pin, amount):
       # ანგარიშიდან თანხის გამოტანის ფუნქცია
        if self.accounts[pin]['balance'] >= amount:
            self.accounts[pin]['balance'] -= amount
            self.save_accounts()
            return True
        else:
            return False

atm = ATM()

def main():
    while True:
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Exit")

        operation = input("Enter your operation: ")

        # ბალანსის შემოწმების ფუნქციის გამოძახება
        if operation == "1":
            pin = input("Enter PIN: ")
            if pin in atm.accounts:
                balance = atm.check_balance(pin)
                print(f"Your balance is: ${balance}")
            else:
                print("Invalid PIN.")

        # თანხის გატანის ფუნქციის გამოძახება
        elif operation == "2":
            pin = input("Enter PIN: ")
            if pin in atm.accounts:
                amount = float(input("Enter withdrawal amount: "))
                if atm.withdraw(pin, amount):
                    print("Withdrawal successful.")
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid PIN.")

        elif operation == "3":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



