from muapi import MuAPI

client = MuAPI()

result = client.edit.effects(
    video_url="VIDEO_URL",
    effect="anime",
    wait=False
)

print(result)