import pytest

from bank_system.bank_account.checking_account import CheckingAccount


def test_invalid_init_instance():
    with pytest.raises(ValueError):
        CheckingAccount("Mai", -1)

def test_withdraw():
    bank_account = CheckingAccount("Mai", 10)
    bank_account.deposit(100)
    bank_account.withdraw(40)
    assert bank_account.account_info()[1] == 50