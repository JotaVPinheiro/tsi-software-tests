from validar_vouncher import validar_voucher


def test_return_false_for_values_below_50():
    assert validar_voucher(49.00) == False
    assert validar_voucher(49.99) == False


def test_return_true_for_exactly_50():
    assert validar_voucher(50.00) == True


def test_return_true_for_values_above_50():
    assert validar_voucher(50.01) == True
    assert validar_voucher(51.00) == True


def test_return_true_for_values_below_500():
    assert validar_voucher(499.00) == True
    assert validar_voucher(499.99) == True


def test_return_true_for_exactly_500():
    assert validar_voucher(500.00) == True


def test_return_false_for_values_above_500():
    assert validar_voucher(500.01) == False
    assert validar_voucher(501.00) == False
