from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_blue, ft_green, ft_grey
import matplotlib.pyplot as plt
import numpy as np

array = ft_load("../landscape.jpg")

print(array)

np_inverted = ft_invert(array)
np_red = ft_red(array)
np_green = ft_green(array)
np_blue = ft_blue(array)
np_grey = ft_grey(array)

plt.imshow(np_inverted)
plt.show()

plt.imshow(np_red)
plt.show()

plt.imshow(np_green)
plt.show()

plt.imshow(np_blue)
plt.show()

plt.imshow(np_grey)
plt.show()