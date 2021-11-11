import numpy as np
import matplotlib.pyplot as plt
#from ipywidgets import interact, fixed
from PIL import Image


def imshow(X, resize=None):
    """
    You should create a way to resize an image from an array X.
    The use of widgets is optional but you can take a look to interact.
    We should be able to install this package in Google Colab from your Git
    repo.
    """

    img = Image.fromarray(X, 'RGB')

    if resize!=None:
        resizedImg = img.resize(resize)
    else:
        resizedImg = img

    plt.imshow(resizedImg)
    plt.tight_layout()

    pass