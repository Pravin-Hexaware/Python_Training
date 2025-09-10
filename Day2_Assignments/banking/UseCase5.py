import accounts as acc
import transactions as tr

acc.createAccount(101,"pravin",1000)
tr.deposit(101,500)
tr.withdraw(101,200)
print("balance:",acc.getBalance(101))
