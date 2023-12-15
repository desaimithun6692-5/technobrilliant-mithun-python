# compilation error
# logical error
# Runtime error

a = 6
b = 0
print("start")

try:
    # c = a/b
    d = int("p")

except ValueError as e:
    print("I got a value error exception  ", e)
    print("exception end")
except ZeroDivisionError as e:
    print("i got divide by zero ", e)
except Exception as e:
    print("General expectoion occured ", e)

finally:
    print("finally block ")

print("end")
