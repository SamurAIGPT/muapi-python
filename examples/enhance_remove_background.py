from muapi import MuAPI

client = MuAPI()

result = client.enhance.remove_background(
    image_url="https://example.com/image.jpg",
    wait=False
)

print(result)