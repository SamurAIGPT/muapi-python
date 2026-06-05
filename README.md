# MuAPI Python SDK

Official Python SDK for MuAPI.

Generate images, videos, audio, run AI enhancement workflows, upload files, manage predictions, and interact with MuAPI directly from Python.

## Installation

```bash
pip install muapi-python-sdk
```

Or install from source:

```bash
git clone https://github.com/YOUR_USERNAME/muapi-python-sdk.git
cd muapi-python-sdk
pip install -e .
```

## Authentication

Configure your API key:

```python
from muapi import MuAPI

client = MuAPI()
```

The SDK uses the same API key configuration as the MuAPI CLI.

## Image Generation

```python
from muapi import MuAPI

client = MuAPI()

result = client.images.generate(
    prompt="A futuristic city at sunset"
)

print(result)
```

## Image Editing

```python
result = client.images.edit(
    prompt="Convert this image into anime style",
    image="https://example.com/image.jpg"
)

print(result)
```

## Video Generation

```python
result = client.videos.generate(
    prompt="A dragon flying through clouds",
    wait=False
)

print(result)
```

## Image to Video

```python
result = client.videos.from_image(
    prompt="Camera slowly zooms in",
    image="https://example.com/image.jpg",
    wait=False
)

print(result)
```

## Audio Generation

```python
result = client.audio.from_text(
    prompt="Relaxing ocean waves",
    wait=False
)

print(result)
```

## Image Enhancement

```python
result = client.enhance.upscale(
    image_url="https://example.com/image.jpg"
)

print(result)
```

## Background Removal

```python
result = client.enhance.remove_background(
    image_url="https://example.com/image.jpg"
)

print(result)
```

## Video Editing

```python
result = client.edit.lipsync(
    video_url="VIDEO_URL",
    audio_url="AUDIO_URL"
)

print(result)
```

## Upload Files

```python
result = client.uploads.upload(
    "image.png"
)

print(result)
```

## Predictions

```python
result = client.predictions.get(
    "REQUEST_ID"
)

print(result)
```

Wait for completion:

```python
result = client.predictions.wait(
    "REQUEST_ID"
)

print(result)
```

## Models

```python
print(client.models.list())
print(client.models.categories())
```

## Account

```python
print(client.account.balance())
```

## Examples

See the `examples/` directory for complete examples.

## Features

* Images API
* Videos API
* Audio API
* Enhancement API
* Editing API
* Upload API
* Predictions API
* Models API
* Account API

## License

MIT License
