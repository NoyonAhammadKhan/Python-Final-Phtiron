from abc import ABC, abstractmethod


class Bank:
    accountsList = []
    totalBalance = 0
    loanStatus = True
    admin = []

    def __init__(self, admin_email) -> None:
        self.total_assets = 0
        self.users_accounts = [{}]
        self.admin = admin_email
        self.total_loan = 0

    @classmethod
    def checkTotalBalance(cls):
        print(f"Total Assets Of The Bank Is {cls.totalBalance}")

    @staticmethod
    def totalLoanGiven():
        total = 0
        for account in Bank.accountsList:
            total += account.loanAmount

        print(f"Total given loan is {total}")

    @staticmethod
    def showUsers():
        count = 1

        if len(Bank.accountsList) > 0:
            for account in Bank.accountsList:
                print(
                    f"{count}---NAME: {account.name}\n ---EMAIL:{account.email}\n ---ADDRESS: {account.address}")
                count += 1
        else:
            print("No users exists")

    @classmethod
    def deleteAcount(cls, acNumber):
        deleteIndex = 0
        found = False
        for i, account in enumerate(cls.accountsList):
            if account.accountNumber == acNumber:
                deleteIndex = i
                found = True
                cls.accountsList.pop(deleteIndex)
                print(f"The account with {acNumber} is deleted")
                break

        if found == False:
            print(f"The account with {acNumber} doesn't exists")

    @classmethod
    def changeLoanStatus(self, status):
        if self.loanStatus == True and status == 'OFF':
            self.loanStatus = False
            print("The loan is off now.")
        elif self.loanStatus == False and status == 'ON':
            self.loanStatus = True
            print("The loan is on now.")

    @classmethod
    def addToBalance(cls, amount):
        cls.totalBalance += amount

    @classmethod
    def deductToBalance(cls, amount):
        cls.totalBalance -= amount


class Account(ABC):
    isLoan = True
    admin = []

    def __init__(self,  name, email, address, password, accountNumber, type):
        self.name = name
        self.email = email
        self.accountNumber = accountNumber
        self.password = password
        self.balance = 0
        self.address = address
        self.type = type
        self.loanCount = 0
        self.loanAmount = 0
        self.allTransaction = []
        self.isBankRupt = False

        Bank.accountsList.append(self)

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            Bank.addToBalance(amount)
            self.allTransaction.append(
                {"deposit": f"You have deposited {amount}"})
            print(f"\n--> Deposited {amount}. New balance: ${self.balance}")
        else:
            print("\n--> Invalid deposit amount")

    def withdraw(self, amount):
        if self.balance == 0 or self.isBankRupt == True:
            print("n\You are now bankrupt.")

        elif amount >= 0 and amount <= self.balance:
            self.balance -= amount
            Bank.addToBalance(amount)
            self.allTransaction.append(
                {"withdraw": f"You have withdraw {amount}"})
            print(f"\nWithdraw ${amount}. New balance: ${self.balance}")
        else:
            print("\nWithdrawal amount exceeded.")

    def checkBalance(self):
        print(f"Your Balance is: {self.balance}")

    def transferBalance(self, transferableAccountNumber, transferableAmount):
        accountExist = False
        transferableAccount = None
        for account in Bank.accountsList:
            if account.accountNumber == transferableAccountNumber:
                accountExist = True
                transferableAccount = account
                break

        if accountExist:
            self.balance -= transferableAmount
            transferableAccount.balance += transferableAmount
            self.allTransaction.append(
                {"balance-transfer": f"You have transfer amount {transferableAmount} from {self.accountNumber} to {transferableAccountNumber}"})
            print(
                f"You have transfer amount {transferableAmount} from {self.accountNumber} to {transferableAccount.accountNumber}")

        else:
            print(f"{transferableAccountNumber} Account does not exist")

    def takeLoan(self, amount):

        if (self.loanCount >= 2):
            print("Sorry this loan can't be processed. You have already take two loans")

        elif Bank.totalBalance < amount:
            print("The bank have not sufficient amount.")

        else:
            self.loanCount += 1
            self.allTransaction.append({"takeLoan": "You had taken a loan."})
            print(
                f"Your loan has been processed. You have take loan {self.loanCount} times.")

    def checkTransactions(self):
        if len(self.allTransaction) == 0:
            print("You don't have any transaction recorded")
        else:
            for transaction in self.allTransaction:
                print(transaction)


class SavingsAccount(Account):
    def __init__(self, name, email, address, password, accountNumber):
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        super().__init__(name, email, address, password, accountNumber, "savings")


class CurrentAccount(Account):
    def __init__(self,  name, email, address, password, accountNumber):
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        super().__init__(name, email, address, password, accountNumber, "current")
