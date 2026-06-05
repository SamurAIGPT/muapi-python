from muapi import MuAPI

client = MuAPI()

result = client.edit.lipsync(
    video_url="VIDEO_URL",
    audio_url="AUDIO_URL",
    wait=False
)

print(result)