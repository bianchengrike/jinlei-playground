# LBYL vs EAFP: Preventing or Handling Errors in Python

# LBYL
# 一定要可以用了才去用
if "possible_key" in data_dict:
    value = data_dict["possible_key"]
else:
    # Handle missing keys here...

# EAFP
# 能不能用，用了再说
try:
     value = data_dict["possible_key"]
except KeyError:
    # Handle missing keys here...


# Avoiding Unnecessary Check Repetition
def to_integer_LBYL(value):
     if value.isdigit():  # duplicates checks
         return int(value)
     return None


def to_integer_EAFP(value):
     try:
         return int(value)
     except ValueError:
         return None

 