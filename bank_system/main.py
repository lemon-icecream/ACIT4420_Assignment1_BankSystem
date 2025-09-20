from bank_system.bank_account.bank_account import BankAccount
from bank_system.bank_account.checking_account import CheckingAccount
from bank_system.bank_account.savings_account import SavingsAccount


def main():
    bank_account = BankAccount("Mai")
    bank_account.deposit(1000000)
    print(f"Bank account info: {bank_account.account_info()}")

    saving_account = SavingsAccount("Mai")
    saving_account.deposit(100)
    saving_account.apply_interest()
    print(f"Saving account info: {saving_account.account_info()}")

    checking_account = CheckingAccount("Mai")
    checking_account.deposit(100)
    checking_account.withdraw(98)
    print(f"Checking account info: {checking_account.account_info()}")

if __name__ == "__main__":
    main()