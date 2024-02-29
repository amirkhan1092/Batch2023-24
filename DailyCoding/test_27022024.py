import test_27022024


def test_is_balanced():
    # Test cases with balanced parentheses
    assert is_balanced("") == True
    assert is_balanced("()") == True
    assert is_balanced("()()") == True
    assert is_balanced("(())") == True
    assert is_balanced("((()))") == True
    assert is_balanced("()()()") == True
    assert is_balanced("(()())") == True
    assert is_balanced("(((())))") == True

    # Test cases with unbalanced parentheses
    assert is_balanced("(") == False
    assert is_balanced(")") == False
    assert is_balanced("(()") == False
    assert is_balanced("())") == False
    assert is_balanced("((()") == False
    assert is_balanced("(()))") == False
    assert is_balanced("((())") == False
    assert is_balanced("(((()))") == False

    print("All test cases pass")

test_is_balanced()