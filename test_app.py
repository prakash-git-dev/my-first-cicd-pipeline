from app import calculate_tax

def test_tax_calculation():
    # If salary is 1000, 20% tax should equal 200
    assert calculate_tax(1000) == 200
