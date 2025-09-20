from bank_system.bank_account.bank_account import BankAccount


class SavingsAccount(BankAccount):

    def __init__(self, account_holder, interest_rate = 0.02):
        super().__init__(account_holder)

        if interest_rate < 0 or interest_rate > 1:
            raise ValueError('Interest rate must be between 0 and 1')
        self.__interest_rate = interest_rate

    def apply_interest(self):
        self._balance *= 1 + self.__interest_rate
