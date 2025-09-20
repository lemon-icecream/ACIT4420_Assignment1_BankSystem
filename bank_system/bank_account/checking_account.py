from typing import override
from bank_system.bank_account.bank_account import BankAccount


class CheckingAccount(BankAccount):

    def __init__(self, account_holder, transaction_fee = 1.0):
        super().__init__(account_holder)

        if transaction_fee < 0:
            raise ValueError('Transaction fee cannot be negative')
        self.__transaction_fee = transaction_fee

    @override
    def withdraw(self, amount: float):
        super().withdraw(amount + self.__transaction_fee)
