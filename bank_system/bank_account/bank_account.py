class BankAccount:

    def __init__(self, account_holder: str):
        if not isinstance(account_holder, str):
            raise TypeError('Name of the account holder must be a string')
        if not account_holder.strip():
            raise ValueError('Name of the account holder must be provided')
        self.__account_holder = account_holder
        self._balance = 0.0

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive')
        self._balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError('Withdraw amount must be positive')
        if amount > self._balance:
            raise ValueError('Withdraw amount (plus transaction fee if there is) cannot be greater than the balance')
        self._balance -= amount

    def account_info(self) -> tuple[str, float]:
        return self.__account_holder, self._balance