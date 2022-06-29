
try:
    print(1 / 0)
except ZeroDivisionError:
    print("ZeroDivisionError")
else:
    print("else")  # else is executed if no exception is raised
finally:
    # finally is executed regardless of the exception raised or not
    print("finally ZeroDivisionError case")

try:
    print(1 / 10)
except ZeroDivisionError:
    print("ZeroDivisionError")
else:
    # else is executed if no exception is raised
    print("else(no ZeroDivisionError case)")
finally:
    # finally is executed regardless of the exception raised or not
    print("finally no ZeroDivisionError case")
