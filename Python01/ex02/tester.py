from load_image import ft_load

print(ft_load("../landscape.jpg"))
print(ft_load("../animal.jpeg"))

try:
    print(ft_load("../animale.jpeg"))
except AssertionError as e:
    print(e.args[0])
