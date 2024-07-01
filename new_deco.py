def deco_to_upper(to_upper):
    def wrapper(n):
        result = to_upper(n).upper()
        return result
    return wrapper

@deco_to_upper
def to_upper(name):
    return name

n = "darshan"
result = to_upper(n)  # Call the decorated function
print(result)  # Output: DARSHAN