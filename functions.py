# function is block of code hat can be called from any where

# #defination of functions
# def print_hello():
#     print("hello world ")
#     print("hello world 2")
#
#
#
#
# print("hi")
# print("start")
# print_hello() # calling a function
# print("done")

# paramerterized function

def print_hello_paremeter(name, last):
    print(f"hello world {name} ")
    print(f"hello world 2 {last}")


print("hi")
print("start")
print_hello_paremeter(last="naik", name="ram")  # calling a function
print("done")


# return value

def calculate_simple_interest(principle, interest, years):
    return (principle * interest * years) / 100


def return_value():
    return 10


variable = return_value()
print(variable)
print(return_value())
value = calculate_simple_interest(1000, 10, 2)
print(value)


def print_hello(name="default"):
    print(f"hello world {name} ")


print_hello("ram")
print_hello()

# create a function to calculate multiplication  return /
# create list retrun sum

