from Bank import SavingsAccount, CurrentAccount, Account, Bank
from Users import Admin

currentUser = None


while (True):
    if currentUser == None:
        print("\n--> No user logged in !")
        ch = input("\n--> Register/Login (R/L) : ")
        if ch == "R":
            ch = input("\n--> Register for User or Admin (U/A) : ")
            if ch == "U":
                name = input("Name: ")
                email = input("Email: ")
                address = input("Address: ")
                password = input("Password:")
                ac_type = input(
                    "Savings Account or special Account (sv/curr) :")
                if ac_type == "sv":
                    accountNumber = len(Bank.accountsList)+1
                    currentUser = SavingsAccount(
                        name, email, address, password, accountNumber)
                    print(
                        f"Your Account Number is {accountNumber}. Please collect it for future refererence")
                elif ac_type == "curr":
                    accountNumber = len(Bank.accountsList)+1
                    currentUser = CurrentAccount(
                        name, email, address, password, accountNumber)
                    print(
                        f"Your Account Number is {accountNumber}. Please collect it for future refererence")
            elif ch == "A":
                name = input("Name: ")
                email = input("Email: ")
                password = input("Password: ")
                accountNumber = len(Bank.admin)+1
                currentUser = Bank.admin.append(Admin(
                    name,
                    email,
                    password,
                    accountNumber,
                    "admin"
                ))
                currentUser = Bank.admin[accountNumber-1]

                print(
                    f"Your Account Number is {accountNumber}. Please collect it for future refererence")
        else:
            ac_type = input("Account type is USER or ADMIN (U/A)")
            ac_no = int(input("Account Number:"))

            if ac_type == "U":
                for account in Bank.accountsList:
                    if account.accountNumber == ac_no:
                        currentUser = account
                        break
            elif ac_type == "A":
                for account in Bank.admin:
                    if account.accountNumber == ac_no:
                        currentUser = account
                        break

    else:

        if currentUser.type == "savings" or currentUser.type == "current":
            print(f"\nWelcome {currentUser.name} !\n")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Check Balance")
            print("4. Check Transactions")
            print("5. Take Loan")
            print("6. Transfer Balance")
            print("7. Logout")
            print("8. Exit\n")

            op = int(input("Chose Required Option:"))

            if op == 1:
                amount = int(input("Enter deposit amount:"))
                currentUser.deposit(amount)

            elif op == 2:
                amount = int(input("Enter withdraw amount:"))
                currentUser.withdraw(amount)

            elif op == 3:
                currentUser.checkBalance()

            elif op == 4:
                currentUser.checkTransactions()

            elif op == 5:
                amount = int(input("Enter loan amount:"))
                currentUser.takeLoan(amount)

            elif op == 6:
                transferableAccount = int(input(
                    "Which account do you want to transfer money: "))
                transferableAmount = int(input("Please put the amount: "))
                currentUser.transferBalance(
                    transferableAccount, transferableAmount)
            elif op == 7:
                currentUser = None

            elif op == 8:
                break

            else:
                print("Invalid Option")

        else:

            print(f"\nWelcome {currentUser.name} !\n")
            print("1.Delete Any User Account")
            print("2.See All User Account List")
            print("3.Check The Total Available Balance Of The Bank")
            print("4.Can Check The Total Loan Amount")
            print("5.On/Off the loan feature of the bank ")
            print("6. Logout")
            print("7. Exit\n")

            op = int(input("Chhose Option:"))

            if op == 1:
                ac = int(input("Enter the bank AC Number:"))
                decision = input("Do you really want to delete this?(Y/N)")
                if decision == "Y":
                    Bank.deleteAcount(ac)
                else:
                    continue

            # done
            elif op == 2:
                Bank.showUsers()

            # done
            elif op == 3:
                Bank.checkTotalBalance()

            # done
            elif op == 4:
                Bank.totalLoanGiven()

            # done
            elif op == 5:
                if (Bank.loanStatus == True):
                    print("Current Status Of Loan is On")
                elif (Bank.loanStatus == False):
                    print("Current Status Of Loan is Off")
                decision = input("On/Off----(ON/OFF)")
                if decision == "ON":
                    Bank.changeLoanStatus("ON")
                elif decision == "OFF":
                    Bank.changeLoanStatus("OFF")
            # done
            elif op == 6:
                currentUser = None

            # done
            elif op == 7:
                break
            # done
            else:
                print("Invalid Option")
