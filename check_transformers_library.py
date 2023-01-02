# Import the transformers library
import transformers
import datasets
import gradio as gr
import pydub

# Print the version of the transformers library
print(transformers.__version__)
print(datasets.__version__)
print(gr.__version__)
#print(pydub.__version__)
print("In the name of GOD")
print("Date: 2-Janyuary-2023")

import os
import gradio as gr
import torch
import pydub
import torchaudio
from torchaudio.sox_effects import apply_effects_tensor
import numpy as np
from transformers import AutoFeatureExtractor, AutoModelForAudioXVector

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#print(f"I'm learning {language} from {school}.")
print(f"device = {device} .")