class BaseAcct:
    def __init__(self):
        self.rate_of_intertest = 10


    def get_balance(self):
        print("balance from Base class")


class SavingAcct(BaseAcct):


    def get_saving_balance(self):
        print("balance from saving account class")


class CurrentAcct(BaseAcct):

    def get_credit(self):
        pass


class SalaryAcct(BaseAcct):

    def get_reward_point(self):
        pass


acct = SavingAcct()
acct.get_balance()
print(acct.rate_of_intertest)
