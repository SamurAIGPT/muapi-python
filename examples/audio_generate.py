from muapi import MuAPI

client = MuAPI()

result = client.audio.from_text(
    prompt="Relaxing ocean waves",
    wait=False
)

print(result)