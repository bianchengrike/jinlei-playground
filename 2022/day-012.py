# Using Python’s and Operator in Non-Boolean Contexts
a_list = ["expected value", "other value"]
flag = False

if len(a_list) > 0 and a_list[0] == "expected value":
    flag = True

# better way to do it
flag = len(a_list) > 0 and a_list[0] == "expected value"

number = 7

if number > 0:
    if number < 10:
            # Do some calculation with number...
        print("Calculation done!")

# better way to do it
if number > 0 and number < 10:
    print("Calculation done!")

