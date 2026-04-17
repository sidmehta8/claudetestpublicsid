from calculator import Calculator

def test_initial_display():
    c = Calculator()
    assert c.display == "0"

def test_digit_input():
    c = Calculator()
    c.input_digit("5")
    assert c.display == "5"

def test_multiple_digits():
    c = Calculator()
    c.input_digit("1")
    c.input_digit("2")
    assert c.display == "12"

def test_addition():
    c = Calculator()
    c.input_digit("3")
    c.input_operator("+")
    c.input_digit("4")
    c.equals()
    assert c.display == "7"

def test_subtraction():
    c = Calculator()
    c.input_digit("9")
    c.input_operator("-")
    c.input_digit("3")
    c.equals()
    assert c.display == "6"

def test_multiplication():
    c = Calculator()
    c.input_digit("6")
    c.input_operator("*")
    c.input_digit("7")
    c.equals()
    assert c.display == "42"

def test_division():
    c = Calculator()
    c.input_digit("8")
    c.input_operator("/")
    c.input_digit("2")
    c.equals()
    assert c.display == "4"

def test_division_by_zero():
    c = Calculator()
    c.input_digit("5")
    c.input_operator("/")
    c.input_digit("0")
    c.equals()
    assert c.display == "Error"

def test_clear():
    c = Calculator()
    c.input_digit("9")
    c.clear()
    assert c.display == "0"

def test_toggle_sign():
    c = Calculator()
    c.input_digit("5")
    c.toggle_sign()
    assert c.display == "-5"

def test_percent():
    c = Calculator()
    c.input_digit("5")
    c.percent()
    assert c.display == "0.05"

def test_decimal():
    c = Calculator()
    c.input_digit("3")
    c.input_decimal()
    c.input_digit("5")
    assert c.display == "3.5"

def test_chained_operations():
    c = Calculator()
    c.input_digit("3")
    c.input_operator("+")
    c.input_digit("4")
    c.input_operator("+")  # triggers intermediate eval
    c.input_digit("2")
    c.equals()
    assert c.display == "9"

def test_integer_display():
    c = Calculator()
    c.input_digit("4")
    c.input_operator("/")
    c.input_digit("2")
    c.equals()
    assert c.display == "2"  # not "2.0"
