from muapi import MuAPI

client = MuAPI()

result = client.videos.from_image(
    prompt="Camera slowly zooms in",
    image="https://example.com/image.jpg",
    wait=False
)

print(result)