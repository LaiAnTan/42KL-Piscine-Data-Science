import numpy as np
from typing import Any


def ft_invert(array: np.ndarray[(Any, Any, 3), np.int_]) \
        -> np.ndarray[(Any, Any, 3), np.int_]:
    """
    Inverts an image's colour.

    @param array: NumPy NDarray containing rgb data on the image
    @return nd_invert: NumPy NDarray containing rgb data on the image after
    inversion
    """
    nd_invert = 255 - array.copy()
    return nd_invert


def ft_red(array: np.ndarray[(Any, Any, 3), np.int_]) \
        -> np.ndarray[(Any, Any, 3), np.int_]:
    """
    Tints an image red.

    @param array: NumPy NDarray containing rgb data on the image
    @return nd_red: NumPy NDarray containing rgb data on the image after
    tinting red
    """
    nd_red = array.copy()
    nd_red[:, :, 1:3] = 0
    return nd_red


def ft_green(array: np.ndarray[(Any, Any, 3), np.int_]) \
        -> np.ndarray[(Any, Any, 3), np.int_]:
    """
    Tints an image green.

    @param array: NumPy NDarray containing rgb data on the image
    @return nd_green: NumPy NDarray containing rgb data on the image after
    tinting green
    """
    nd_green = array.copy()
    nd_green[:, :, 0:3:2] = 0
    return nd_green


def ft_blue(array: np.ndarray[(Any, Any, 3), np.int_]) \
        -> np.ndarray[(Any, Any, 3), np.int_]:
    """
    Tints an image blue.

    @param array: NumPy NDarray containing rgb data on the image
    @return nd_green: NumPy NDarray containing rgb data on the image after
    tinting green
    """
    nd_blue = array.copy()
    nd_blue[:, :, 0:2] = 0
    return nd_blue


def ft_grey(array: np.ndarray[(Any, Any, 3), np.int_]) \
        -> np.ndarray[(Any, Any, 3), np.int_]:
    """
    Converts an image into grayscale.

    @param array: NumPy NDarray containing rgb data on the image
    @return nd_grey: NumPy NDarray containing rgb data on the image after
    conversion to grayscale
    """
    nd_grey = array.copy()
    nd_grey[:, :, :] = np.mean(nd_grey, axis=2, keepdims=True)

    nd_grey = nd_grey.astype(int)
    return nd_grey
