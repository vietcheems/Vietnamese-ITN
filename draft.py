import pynini
import sys
from nemo_text_processing.inverse_text_normalization.inverse_normalize import InverseNormalizer

print(InverseNormalizer().inverse_normalize("hai triệu phẩy không một lớn hơn hai triệu", verbose=True))
