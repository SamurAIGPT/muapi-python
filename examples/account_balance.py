from muapi import MuAPI

client = MuAPI()

balance = client.account.balance()

print(balance)