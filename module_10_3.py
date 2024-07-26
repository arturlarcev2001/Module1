from threading import Thread, Lock

lock = Lock()

class BankAccount:

    def __init__(self):
        self.account = 1000

    def deposit(self, amount):
        self.account += amount
        print("Deposited {}. New balance is {}".format(amount, self.account))

    def withdraw(self, amount):
        self.account -= amount
        print("Withdraw {}. New balance is {}".format(amount, self.account))


def deposit_task(account, amount):
  for _ in range(5):
    lock.acquire()
    account.deposit(amount)
    lock.release()

def withdraw_task(account, amount):
  for _ in range(5):
    lock.acquire()
    account.withdraw(amount)
    lock.release()

def main():
    account = BankAccount()
    deposit_thread = Thread(target=deposit_task, args=(account, 100))
    withdraw_thread = Thread(target=withdraw_task, args=(account, 150))
    deposit_thread.start()
    withdraw_thread.start()
    deposit_thread.join()
    withdraw_thread.join()

main()
