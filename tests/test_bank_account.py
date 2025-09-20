import pytest

from bank_system.bank_account.bank_account import BankAccount
from bank_system.bank_account.checking_account import CheckingAccount
from bank_system.bank_account.savings_account import SavingsAccount


@pytest.mark.parametrize("cls", [BankAccount, CheckingAccount, SavingsAccount])
def test_valid_init_instance(cls):
    bank_account = cls("Mai")
    assert isinstance(bank_account, cls)

@pytest.mark.parametrize("cls, account_holder, expected_error", [
    (BankAccount, 123, TypeError),
    (CheckingAccount, "", ValueError),
    (SavingsAccount, "    ", ValueError)
])
def test_invalid_init_instance(cls, account_holder, expected_error):
    with pytest.raises(expected_error):
        cls(account_holder)

@pytest.mark.parametrize("cls", [BankAccount, CheckingAccount, SavingsAccount])
def test_account_info(cls):
    bank_account = cls("Mai")
    assert bank_account.account_info() == tuple(["Mai", 0.0])

@pytest.mark.parametrize("cls, deposit_amount", [
    (BankAccount, 123),
    (CheckingAccount, 32),
    (SavingsAccount, 11)
])
def test_valid_deposit(cls, deposit_amount):
    bank_account = cls("Mai")
    bank_account.deposit(deposit_amount)
    assert bank_account.account_info()[1] == deposit_amount

@pytest.mark.parametrize("cls, deposit_amount, expected_error", [
    (BankAccount, 0, ValueError),
    (CheckingAccount, -1, ValueError),
    (SavingsAccount, -2, ValueError)
])
def test_invalid_deposit(cls, deposit_amount, expected_error):
    bank_account = cls("Mai")
    with pytest.raises(expected_error):
        bank_account.deposit(deposit_amount)

@pytest.mark.parametrize("cls, deposit_amount, withdraw_amount", [
    (BankAccount, 123, 10),
    (SavingsAccount, 11, 5)
])
def test_valid_withdraw(cls, deposit_amount, withdraw_amount):
    bank_account = cls("Mai")
    bank_account.deposit(deposit_amount)
    bank_account.withdraw(withdraw_amount)
    assert bank_account.account_info()[1] == deposit_amount - withdraw_amount

@pytest.mark.parametrize("cls, deposit_amount, withdraw_amount, expected_error", [
    (BankAccount, 100, 0, ValueError),
    (BankAccount, 100, -1, ValueError),
    (SavingsAccount, 100, 101, ValueError)
])
def test_invalid_withdraw(cls, deposit_amount, withdraw_amount, expected_error):
    bank_account = cls("Mai")
    bank_account.deposit(deposit_amount)
    with pytest.raises(expected_error):
        bank_account.withdraw(withdraw_amount)

