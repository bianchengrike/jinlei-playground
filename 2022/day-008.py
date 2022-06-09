# Python's assert 101

if __debug__:
    if not expression:
        raise AssertionError(assertion_message)

# Equivalent to
assert expression, assertion_message

	 	