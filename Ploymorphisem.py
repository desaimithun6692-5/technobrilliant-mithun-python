# static ploymorsphism
# method overloading
def method1(test, test2, test3=""):
    print(test)


# method1("test11", "", "")
# method1("test12", "", )


# method overridding
class D:

    def perform_something(self):
        print("method in class D")


class A:

    def perform_something(self):
        print("method in class a ")

    def dummy(self):
        print("dumm")


class B(A):

    def perform_something(self):
        print("method in class B")


class C(B, D):
    pass


obj = C()
obj.perform_something()


# obj = A()
# obj.method()


# encapsulation
# not implemented python
class abc:

    def __init__(self):
        self.a = "abc"

    def get_a(self):
        return self.a

    def set_a(self, value):
        self.a = value


obj1 = abc()
obj1.set_a("123")
print(obj1.get_a())


# Data Abstartction


class BankInter:

    def create_account(self):
        pass

    def get_loan(self):
        pass


class CITIBank(BankInter):

    def create_account(self):
        print("create account in CITI")

    def get_loan(self):
        print("Loan in CITI")


class SBIBank(BankInter):

    def create_account(self):
        print("create account in SBI")

    def get_loan(self):
        print("Loan in SBI")


bankacct = SBIBank()

bankacct.create_account()
bankacct.get_loan()