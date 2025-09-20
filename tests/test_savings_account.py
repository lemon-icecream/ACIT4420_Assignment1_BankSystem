import pytest

from bank_system.bank_account.savings_account import SavingsAccount

@pytest.mark.parametrize("interest_rate", [-1, 1.1, 2])
def test_invalid_init_instance(interest_rate):
    with pytest.raises(ValueError):
        SavingsAccount("Mai", interest_rate)

@pytest.mark.parametrize("interest_rate, deposit_amount", [
    (0.01, 100),
    (0.99, 1),
    (0, 100)
])
def test_apply_interest(interest_rate, deposit_amount):
    bank_account = SavingsAccount("Mai", interest_rate)
    bank_account.deposit(deposit_amount)
    bank_account.apply_interest()
    assert bank_account.account_info()[1] == deposit_amount + deposit_amount * interest_rate