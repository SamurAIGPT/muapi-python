from muapi import MuAPI

client = MuAPI()

print(client.models.categories())
print(client.models.list("image"))