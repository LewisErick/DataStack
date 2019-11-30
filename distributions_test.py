from distributions import get_distribution

def distributions_test_x_none():
    try:
        get_distribution(None, [])
    except Exception as e:
        assert(e.args == ('Excepting array-like type, received', "<class 'NoneType'>", 'instead.'))
        return True
    return False

def distributions_test_columns_none():
    try:
        get_distribution([], None)
    except Exception as e:
        assert(str(e) == "object of type 'NoneType' has no len()")
        return True
    return False

distributions_test_x_none()
distributions_test_columns_none()