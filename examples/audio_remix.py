from muapi import MuAPI

client = MuAPI()

result = client.audio.remix(
    song_id="SONG_ID",
    prompt="Make it more energetic",
    wait=False
)

print(result)