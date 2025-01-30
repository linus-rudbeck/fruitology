from app.functions import addition, subtraction, is_even, append_strings

def test_addition():
    result = addition(1, 2) # Call the function we are testing
    assert result == 3 # Check the result

def test_subtraction():
    result = subtraction(10, 5)
    assert result == 5

def test_append_strings():
    result = append_strings("Li", "nus")
    assert result == "Linus"

def test_is_even():
    even_result = is_even(16)
    odd_result = is_even(15)
    assert even_result == True
    assert odd_result == False

def test_is_even_even():
    result = is_even(8)
    assert result == True

def test_is_even_odd():
    result = is_even(7)
    assert result == False



# Flera asserts
# Flera tester
# Mocking & Fixtures & Dependency injection
# Hur mycket testning krävs?
# Hitta alla fel!