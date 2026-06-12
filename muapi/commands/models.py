from .image import T2I_MODELS, I2I_MODELS
from .video import T2V_MODELS, I2V_MODELS

_ALL_MODELS = {
    "text_to_image": T2I_MODELS,
    "image_to_image": I2I_MODELS,
    "text_to_video": T2V_MODELS,
    "image_to_video": I2V_MODELS,
}